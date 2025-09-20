<< Blockchain Wallet Transaction Tracer>>

A Python tool to trace wallet activity across EVM-compatible blockchains.
It fetches transactions for any address, normalizes them, and builds a graph of wallet interactions for visualization and analysis.

 Features

Fetches normal ETH/native transfers and ERC-20 token transfers

Normalizes raw blockchain data into human-readable format

Builds graph structures of wallet interactions (using networkx)

Simple CLI to run from your terminal

Supports export for further analytics (CSV/JSON/visuals)

📂 Project Structure
wallet-tracer/
│
├── src/
│   ├── main.py         # Entry point (CLI runner)
│   ├── fetcher.py      # Fetch transactions from Etherscan-like APIs
│   ├── parser.py       # Normalize and clean transactions
│   ├── visualizer.py   # Build graph/network analysis
│   ├── config.py       # Loads API key from .env
│   └── __init__.py     # Marks src as a package
│
├── .env.example        # Template for API key storage
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

⚙️ Installation

Clone the repository

Set up dependencies

pip install -r requirements.txt

Configure environment variables

Add your API key inside:

ETHERSCAN_API_KEY=your_api_key_here


Run the tracer with:

python -m src.main

It will:

Ask for a wallet address

Fetch transactions via Etherscan API

Normalize the results

Build and optionally visualize the graph

🌍 Supported Chains

Currently works with EVM-compatible chains using EtherScan APIs:


⚠️ Disclaimer

This tool is for educational and research purposes only.

Do NOT use it on networks, wallets, or assets you do not own or have explicit permission to analyze.

Always comply with your jurisdiction’s laws and regulations.

🛠 Future Plans

Add token USD valuation via CoinGecko API

Multi-hop tracing (A → B → C flows)

Support for non-EVM chains (Sui, Solana, Bitcoin)

Interactive web dashboard

📜 License

MIT License – free to use, modify, and share.
