import requests
from agents import function_tool

@function_tool
def get_crypto_price(symbol: str) -> str:
    """
    Get the current market price of a cryptocurrency using CoinLore API.
    User can type simple symbols like BTC, ETH, DOGE.
    """
    try:
        
        response = requests.get("https://api.coinlore.net/api/tickers/")
        response.raise_for_status()
        coins = response.json().get("data", [])

        
        matched = next(
            (coin for coin in coins if coin["symbol"].lower() == symbol.lower()),
            None
        )

        if not matched:
            return f"⚠️ Sorry, I couldn't find a coin with symbol `{symbol.upper()}`."

        name = matched["name"]
        price = matched["price_usd"]

        return f"💰 **{name} ({symbol.upper()})** is currently trading at **${price} USD**."

    except Exception as e:
        return f"❌ Error while fetching price: {e}"
