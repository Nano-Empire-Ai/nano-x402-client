import requests
import time

class NanoX402Client:
    def __init__(self, private_key: str):
        self.private_key = private_key
        
    def _pay_toll(self, pay_to: str, amount: float, network: str):
        # Stub for Solana/Base transaction settlement
        print(f"Executing {network} transaction: {amount} USDC to {pay_to}")
        time.sleep(1) # Simulate network propagation
        return "mock_tx_signature_8f9a2b"

    def post(self, url: str, json: dict):
        """
        Drop-in replacement for requests.post that handles HTTP 402 challenges.
        """
        response = requests.post(url, json=json)
        
        if response.status_code == 402 and "x402-pay-to" in response.headers:
            pay_to = response.headers.get("x402-pay-to")
            price = float(response.headers.get("x402-price", 0))
            network = response.headers.get("x402-network")
            
            print(f"[NanoX402] Payment Required: {price} USDC on {network}")
            
            # Autonomously settle the tollbooth payment
            tx_sig = self._pay_toll(pay_to, price, network)
            
            print("[NanoX402] Payment settled. Retrying request with cryptographic proof.")
            headers = {"Authorization": f"Bearer {tx_sig}"}
            return requests.post(url, json=json, headers=headers)
            
        return response
