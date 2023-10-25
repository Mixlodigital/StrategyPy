"""
    API Documentation
    https://bybit-exchange.github.io/docs/linear/#t-introduction
"""

# API Imports
from pybit import usdt_perpetual

# CONFIG
mode = "production"
timeframe = 60
kline_limit = 200
z_score_window = 21

# LIVE API
api_key_mainnet = "KT7vYOMXTsD3LKOW4o"
api_secret_mainnet = "Eex9sWcrIuE8wCftWrz0AbZIqKyoLqnkmOq1"

# TEST API
api_key_testnet = ""
api_secret_testnet = ""

# SELECTED API
api_key = api_key_testnet if mode == "test" else api_key_mainnet
api_secret = api_secret_testnet if mode == "test" else api_secret_mainnet

# SELECTED URL
api_url = "https://api-testnet.bybit.com" if mode == "test" else "https://api.bybit.com"

# SESSION Activation
session = usdt_perpetual.HTTP(
    endpoint=api_url,
    api_key=api_key,
    api_secret=api_secret
)
