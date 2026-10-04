import json
import os
from urllib import request
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
if not api_key:
    raise RuntimeError(
        "ALPHA_VANTAGE_API_KEY is not set. "
        "Create one at https://www.alphavantage.co/support/#api-key"
    )

def get_cryptocurrency_rate(from_currency, amount):
    url = (
        "https://www.alphavantage.co/query?"
        "function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={from_currency}&"
        f"to_currency=EUR&"
        f"apikey={api_key}"
    )

    with request.urlopen(url, timeout=30) as response:
        data = json.load(response)

    if "Error Message" in data:
        raise ValueError(f"Error fetching exchange rates: {data['Error Message']}")

    exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    converted_amount = exchange_rate * amount

    return {
        "from_currency": from_currency,
        "to_currency": "EUR",
        "amount": amount,
        "exchange_rate": exchange_rate,
        "converted_amount": converted_amount
    }



