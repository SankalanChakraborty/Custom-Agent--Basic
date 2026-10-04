import json

import requests
from dotenv import load_dotenv
import os

load_dotenv()



def get_flight_info():
    params = {
        "access_key": os.getenv("AVIATIONSTACK_API_KEY"), 
    }
    try:
        response = requests.get(os.getenv("AVIATIONSTACK_URI") + "/v1/flights", params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"An error occurred while fetching flight data: {e}")
        return json.dumps({
            "message": "An error occurred while fetching flight data.", "error": str(e)
        })

    return json.dumps({
        "message": "Flight data fetched successfully.",
        "data": response.json()
    })