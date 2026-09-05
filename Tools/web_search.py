import requests
import json
import os

url = "https://api.langsearch.com/v1/web-search"

def search(query):
    payload = json.dumps({
    "query": query,
    "freshness": "noLimit",
    "summary": True,
    "count": 10
    })
    headers = {
    'Authorization': f'Bearer {os.getenv("LANGSEARCH_API_KEY")}',
    'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"An error occurred while fetching web search results: {e}")
        return json.dumps({
            "message": "An error occurred while fetching web search results.", "error": str(e)
        })

    print(response.text)
    return json.dumps({
        "message": "Web search completed successfully.",
        "data": response.json()
    })