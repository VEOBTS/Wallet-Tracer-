# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
INFURA_PROJECT_ID = os.getenv("INFURA_PROJECT_ID")
DEFAULT_CHAIN = os.getenv("DEFAULT_CHAIN", "ethereum")
