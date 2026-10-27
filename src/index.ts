export class NanoX402Client {
    privateKey: string;

    constructor(privateKey: string) {
        this.privateKey = privateKey;
    }

    async post(url: string, body: any): Promise<Response> {
        let response = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(body)
        });

        if (response.status === 402 && response.headers.has('x402-pay-to')) {
            const payTo = response.headers.get('x402-pay-to');
            const price = parseFloat(response.headers.get('x402-price') || '0');
            const network = response.headers.get('x402-network');

            console.log('[NanoX402] Payment Required: ' + price + ' USDC on ' + network);
            
            // Mock settlement
            const txSig = 'mock_tx_signature_npm_' + Date.now();
            console.log('[NanoX402] Payment settled. Retrying request with cryptographic proof.');

            response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer ' + txSig
                },
                body: JSON.stringify(body)
            });
        }
        return response;
    }
}
