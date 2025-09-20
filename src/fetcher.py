# src/fetcher.py
import requests
import time
from typing import List, Dict
from .config import ETHERSCAN_API_KEY
from tqdm import tqdm

ETHERSCAN_BASE = "https://api.etherscan.io/api"

def fetch_normal_txs(address: str, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc"):
    """
    Uses Etherscan 'account' module to fetch normal txs.
    Returns list of tx dicts.
    """
    all_txs = []
    page_i = 1
    while True:
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page_i,
            "offset": offset,
            "sort": sort,
            "apikey": ETHERSCAN_API_KEY
        }
        resp = requests.get(ETHERSCAN_BASE, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if data["status"] != "1":
            # status == 0 may mean no txs or error
            if data.get("message", "").lower().startswith("no records"):
                break
            else:
                raise ValueError(f"Etherscan error: {data}")
        txs = data["result"]
        if not txs:
            break
        all_txs.extend(txs)
        if len(txs) < offset:
            break
        page_i += 1
        time.sleep(0.2)
    return all_txs

def fetch_erc20_txs(address: str, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc"):
    """
    ERC-20 token transfers (token transfers)
    """
    all_txs = []
    page_i = 1
    while True:
        params = {
            "module": "account",
            "action": "tokentx",
            "address": address,
            "startblock": startblock,
            "endblock": endblock,
            "page": page_i,
            "offset": offset,
            "sort": sort,
            "apikey": ETHERSCAN_API_KEY
        }
        resp = requests.get(ETHERSCAN_BASE, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        if data["status"] != "1":
            if data.get("message", "").lower().startswith("no records"):
                break
            else:
                raise ValueError(f"Etherscan error: {data}")
        txs = data["result"]
        if not txs:
            break
        all_txs.extend(txs)
        if len(txs) < offset:
            break
        page_i += 1
        time.sleep(0.2)
    return all_txs
