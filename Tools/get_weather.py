import json

import requests
from dotenv import load_dotenv
import os


load_dotenv()

def get_weather(latitude, longitude):

    params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m"
}
    try:
        response = requests.get(os.getenv("OPEN_METEO_URI"), params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")
        return json.dumps({
            "message": "An error occurred while fetching weather data.", "error": str(e)
        })

    return json.dumps({
        "message": "Weather data fetched successfully.",
        "data": response.json()
    })
