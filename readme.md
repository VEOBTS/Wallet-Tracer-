# Blockchain Wallet Transaction Tracer 

A Python tool to trace wallet activity across EVM-compatible blockchains.
It fetches transactions for any address, normalizes them, and builds a graph of wallet interactions for visualization and analysis.
*This project analyzes blockchain wallet transactions by fetching data from APIs like Etherscan.*

## Features
- Fetches normal ETH/native transfers and ERC-20 token transfers

- Normalizes raw blockchain data into human-readable format

- Builds graph structures of wallet interactions (using networkx)

- Simple CLI to run from your terminal

- Supports export for further analytics (CSV/JSON/visuals)

# Installation

- Clone the repository

- Set up dependencies

 - pip install -r requirements.txt

- Configure environment variables

- Add your API key inside:

- ETHERSCAN_API_KEY=your_api_key_here


### Run the tracer with:

python -m src.main
