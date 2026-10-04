from Tools.get_weather import get_weather
from Tools.web_search import search
from Tools.get_flight_info import get_flight_info


def vacation_planner(latitude, longitude, destination, start_date, end_date, budget):
    """
    Plans a vacation based on the given parameters.

    Args:
        destination (str): The destination for the vacation.
        start_date (str): The start date of the vacation in YYYY-MM-DD format.
        end_date (str): The end date of the vacation in YYYY-MM-DD format.
        budget (float): The budget for the vacation.

    Returns:
        dict: A dictionary containing the planned vacation details.
    """
    # Placeholder implementation

    # check the weather forecast for the destination during the specified dates (for e.g., if a tornado is expected, the user should be warned)
    # scrape the web for information about the destination, including popular attractions, local cuisine, and cultural events

    weather = get_weather(latitude, longitude)
    severe_weather = []

    if weather:
        forecast = weather.get("forecast", []) if isinstance(weather, dict) else []
        for day in forecast:
            conditions = str(day.get("conditions", "")).lower() if isinstance(day, dict) else ""
            if any(keyword in conditions for keyword in ["tornado", "hurricane", "storm", "blizzard", "heavy rain"]):
                severe_weather.append(day)
        
    search(f"Weather forecast for {destination} from {start_date} to {end_date}")
    # get flight information for the destination (for e.g., if there are no flights available, the user should be warned)
    get_flight_info()

    
    search_results = []

    search_results.append(search(f"Popular attractions in {destination}"))
    
    search_results.append(search(f"Local cuisine in {destination}"))

    search_results.append(search(f"Adventures to do in {destination}"))

    print(f"Search results for popular attractions in {destination}: {search_results}")


    travel_warning = "Weather appears generally suitable for travel." if not severe_weather else "Severe weather is expected during the trip; consider adjusting plans."

    return {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "budget": budget,
        "weather": weather,
        "travel_warning": travel_warning,
        "activities": ["Sightseeing", "Local Cuisine", "Adventures", "Relaxation"]
    }