# Nano x402 Client SDK

A Python client designed for AutoGPT, LangChain, and other autonomous agents to natively negotiate and settle `HTTP 402 Payment Required` challenges using Solana/Base USDC.

## Why?
When autonomous scraping/research loops hit Cloudflare 403s or OpenAI rate limits, they fail. By routing traffic through x402-enabled tollbooths, your agent can pay micro-tolls (0.005 - 0.050 USDC) to bypass blocks dynamically. 

## Usage

The SDK acts as a drop-in replacement for standard `requests` calls. 

```python
from nano_x402_client import NanoX402Client

# Initialize with your agent's wallet
client = NanoX402Client(private_key="YOUR_AGENT_WALLET_KEY")

# 1. Agent hits a protected endpoint.
# 2. Client intercepts the 402, parses the headers, and pays the USDC toll autonomously.
# 3. Client retries with the transaction proof.
response = client.post(
    "https://nanoempireai.com/api/v1/unblock", 
    json={"target": "https://httpbin.org/ip"}
)

print(response.json())
```
