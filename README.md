# Nano x402 Client SDK (`@nanoempireai/nano-x402-client`)

TypeScript and Python client SDK for autonomous agents to intercept `HTTP 402 Payment Required` challenges, parse `PAYMENT-REQUIRED` / `accepts[]` descriptors, and retry with settlement proofs against x402 tollbooths.

![Status: Published on npm (v1.0.0)](https://img.shields.io/badge/npm-%40nanoempireai%2Fnano--x402--client-cb3837)
![Mode: Paper Stub + Live x402 v2 Reference](https://img.shields.io/badge/mode-paper_stub_%2B_live_Base_USDC-3b82f6)
![x402 Settlement Proof: Block 51961194](https://img.shields.io/badge/Base_Mainnet-1_self--test_settled-10b981)
![Outside Paying Customers: 0](https://img.shields.io/badge/outside_paying_customers-0-f59e0b)
![License: MIT](https://img.shields.io/badge/license-MIT-64748b)

---

## 1. Install & Run Today

### TypeScript / Node.js
```bash
npm install @nanoempireai/nano-x402-client
```

```typescript
import { NanoX402Client } from "@nanoempireai/nano-x402-client";

const client = new NanoX402Client(process.env.AGENT_PRIVATE_KEY || "paper-key");
const res = await client.post("https://recallguard-api.vercel.app/api/v1/match", {
  items: [{ name: "Fisher-Price Rock 'n Play", upc: "887961098594" }]
});
console.log(await res.json());
```

### Python
```python
from nano_x402_client import NanoX402Client

client = NanoX402Client(private_key="paper-key")
resp = client.post(
    "https://recallguard-api.vercel.app/api/v1/match",
    json={"items": [{"name": "Baby Monitor", "brand": "VTech"}]},
)
print(resp.json())
```

---

## 2. Machine-Readable Discovery Links

- **Canonical LLM Index (`llms.txt`):** [`https://www.nanoempireai.com/llms.txt`](https://www.nanoempireai.com/llms.txt)
- **A2A Agent Card (`v1.5.0`):** [`https://www.nanoempireai.com/.well-known/agent-card.json`](https://www.nanoempireai.com/.well-known/agent-card.json)
- **Poppy / PAP Manifest (`PAP/1.0`):** [`https://www.nanoempireai.com/.well-known/poppy.json`](https://www.nanoempireai.com/.well-known/poppy.json)
- **Commercial Offers (`offers.json`):** [`https://www.nanoempireai.com/offers.json`](https://www.nanoempireai.com/offers.json)
- **OpenAPI 3.1 Spec:** [`https://www.nanoempireai.com/.well-known/openapi.json`](https://www.nanoempireai.com/.well-known/openapi.json)

---

## 3. Live Target Endpoints & Pricing (`x402 v2` on Base Mainnet)

- **Network:** Base Mainnet (`eip155:8453`)
- **Asset:** USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`)
- **Pay-To Treasury:** `0x90E23A7b6F6494A879d05DDC4278D0e55Dec1e01`

| Endpoint | Method | Price | Status |
|----------|--------|-------|--------|
| `https://recallguard-api.vercel.app/api/v1/health` | `GET` | **Free** | **LIVE** (`46,642` recalls) |
| `https://recallguard-api.vercel.app/api/v1/feed` | `GET` | **$0.05 USDC** (`50000` atomic) | **LIVE** (HTTP 402 active) |
| `https://recallguard-api.vercel.app/api/v1/match` | `POST` | **$0.10 USDC** (`100000` atomic) | **LIVE** (HTTP 402 active) |

---

## 4. Settlement Proof & Honest Status Disclosure

- **SDK Status:** The open-source client wrapper in this repository includes paper-mode simulation helpers for testing 402 retry loops locally; live production settlement against `recallguard-api.vercel.app` uses `x402 v2` EIP-3009 `TransferWithAuthorization` via `https://x402.org/facilitator`.
- **On-Chain Settlement Proof (Base Block `51961194`):** [`0x0581b819b2e5b481cbbcfb8fe81e6fe57a0d0ef9c6f8fc04952164761586da64`](https://basescan.org/tx/0x0581b819b2e5b481cbbcfb8fe81e6fe57a0d0ef9c6f8fc04952164761586da64) (`0.05 USDC` settled).
- **Volume Ledger:** `1` verified self-test settlement on Base Mainnet; `0` outside paying customers to date.

---

## 5. License & Contact

- **License:** MIT
- **Contact:** Robert Lambert (`rob@nanoempireai.com`) · [`https://www.nanoempireai.com`](https://www.nanoempireai.com)
