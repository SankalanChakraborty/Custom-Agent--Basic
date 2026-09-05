import json

import requests
from dotenv import load_dotenv
import os

load_dotenv()

currency_symbol_mapping={
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "INR": "₹",
    "AUD": "A$",
    "CAD": "C$",
    "CHF": "CHF",
    "CNY": "¥",
    "SEK": "kr",
    "NOK": "kr",
    "DKK": "kr",
    "PLN": "zł",
    "CZK": "Kč",
    "HUF": "Ft",
    "RON": "lei",
    "BGN": "лв",
    "HRK": "kn",
    "RSD": "дин.",
    "RUB": "₽",
    "UAH": "₴",
    "TRY": "₺",
    "BRL": "R$",
    "MXN": "MX$",
    "ZAR": "R",
    "SGD": "S$",
    "HKD": "HK$",
    "NZD": "NZ$",
    "KRW": "₩",
    "IDR": "Rp",
    "MYR": "RM",
    "PHP": "₱",
    "THB": "฿",
    "VND": "₫",
    "AED": "د.إ",
    "SAR": "﷼",
    "EGP": "£",
    "ILS": "₪",
    "PKR": "₨",
    "BDT": "৳",
    "LKR": "Rs",
    "NPR": "₨",
    "MVR": ".ރ",
    "BHD": ".د.ب",
    "QAR": "﷼",
    "KWD": "د.ك",
    "OMR": "﷼",
    "JOD": "د.ا",
    "LBP": "ل.ل",
    "IQD": "ع.د",
    "IRR": "﷼",
    "TWD": "NT$",
    "MNT": "₮",
    "KZT": "₸",
    "UZS": "so'm",
    "GEL": "₾",
    "AMD": "֏",
    "BYN": "Br",
    "MDL": "L",
    "ALL": "L",
    "ISK": "kr",
    "GHS": "₵",
    "NGN": "₦",
    "KES": "KSh",
    "TZS": "TSh",
    "UGX": "USh",
    "MAD": "د.م.",
    "DZD": "دج",
    "TND": "د.ت",
    "AOA": "Kz",
    "MZN": "MT",
    "BWP": "P",
    "NAD": "N$",
    "ZWL": "Z$",
    "GMD": "D",
    "XAF": "FCFA",
    "XOF": "CFA",
    "XPF": "₣",
    "CLP": "$",
    "COP": "$",
    "PEN": "S/",
    "ARS": "$",
    "UYU": "$",
    "PYG": "₲",
    "BOB": "Bs",
    "CRC": "₡",
    "GTQ": "Q",
    "HNL": "L",
    "NIO": "C$",
    "PAB": "B/.",
    "DOP": "RD$",
    "JMD": "J$",
    "TTD": "TT$",
    "BBD": "Bds$",
    "BMD": "$",
    "KYD": "CI$",
    "XCD": "EC$",
    "BSD": "$",
    "BND": "B$",
    "KHR": "៛",
    "LAK": "₭",
    "MMK": "Ks",
    "MOP": "MOP$",
    "CUP": "$",
    "DZD": "دج",
}

def get_exchange_rates(from_currency, to_currency, amount):
    url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"An error occurred while fetching exchange rates: {e}")
        return json.dumps({
            "message": "An error occurred while fetching exchange rates.", "error": str(e)
        })

    data = response.json()
    print(data)
    return json.dumps({
        "message": f"{currency_symbol_mapping[to_currency]} {data['rate']*amount}"
    })

