from dotenv import load_dotenv
from google import genai
import json
import os
from Tools.get_cryptocurrency_rate import get_cryptocurrency_rate
from Tools.get_exchange_rate import get_exchange_rates
from Tools.get_weather import get_weather
from Tools.web_search import search
from Tools.create_note import create_note
from Tools.File_Manager.list_files import list_files
from Tools.File_Manager.read_file import read_file
from Tools.File_Manager.create_file import create_file
from Tools.get_flight_info import get_flight_info
from Tools.vacation_planner import vacation_planner

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

history = []

weather_tool = {
    "type": "function",
    "name": "get_weather",
    "description": "Get the currrent weather of a speific location",
    "parameters":{
        "type": "object",
        "properties":{
            "latitude": {
                "type": "number",
                "description": "The latitude of the location"
            },
            "longitude": {
                "type": "number",
                "description": "The longitude of the location"
            }
        },
        "required": ["latitude", "longitude"]
    }
}

currency_converter_tool = {
    "type": "function",
    "name": "get_exchange_rates",
    "description": "Get the exchange rates between two currencies",
    "parameters":{
        "type": "object",
        "properties":{
            "from_currency": {
                "type": "string",
                "description": "The currency to convert from"
            },
            "to_currency": {
                "type": "string",
                "description": "The currency to convert to"
            },
            "amount":{
                "type": "number",
                "description": "The amount to convert"
            }
        },
        "required": ["from_currency", "to_currency", "amount"]
    }

}

web_search_tool = {
    "type": "function",
    "name": "search",
    "description": "Search the web for information",
    "parameters":{
        "type": "object",
        "properties":{
            "query":{
                "type": "string",
                "description": "The search query"
            }
        },
        "required": ["query"]
    }
}

create_note_tool = {
    "type": "function",
    "name": "create_note",
    "description": "Create a note and save it to a file",
    "parameters":{
        "type": "object",
        "properties":{
            "note":{
                "type": "string",
                "description": "The note to be created under Results directory"
            }
        },
        "required": ["note"]
    }
}

list_files_tool = {
    "type": "function",
    "name": "list_files",
    "description": "List all files in a given directory",
    "parameters":{
        "type": "object",
        "properties":{
            "directory":{
                "type": "string",
                "description": "The directory to list files from"
            }
        },
        "required": ["directory"]
    }
}

read_file_tool = {
    "type": "function",
    "name": "read_file",
    "description": "Read the contents of a file",
    "parameters":{
        "type": "object",
        "properties":{
            "path":{
                "type": "string",
                "description": "The path to the file to be read"
            }
        },
        "required": ["path"]
    }
}

create_file_tool = {
    "type": "function",
    "name": "create_file",
    "description": "Create a new file at the specified path with optional content",
    "parameters":{
        "type": "object",
        "properties":{
            "path":{
                "type": "string",
                "description": "The path where the file will be created"
            },
            "content":{
                "type": "string",
                "description": "The content to write to the file (default is empty)"
            },        
        },
        "required": ["path"]
    }
}

get_cryptocurrency_rate_tool = {
    "type": "function",
    "name": "get_cryptocurrency_rate",
    "description": "Get the current exchange rate of a cryptocurrency in a specific currency",
    "parameters":{
        "type":"object",
        "properties":{
            "from_currency":{
                "type":"string",
                "description": "The cryptocurrency to convert from (e.g., BTC, ETH)"
            },
            
            "amount":{
                "type":"number",
                "description": "The amount of the cryptocurrency to convert"
            }
        },
        "required": ["from_currency", "amount"]
    }
}

get_flight_info_tool = {
    "type": "function",
    "name": "get_flight_info",
    "description": "Get the current flight information from the AviationStack API",
    "parameters":{
        "type":"object",
        "properties":{},
        "required": []
    }
}

vacation_planner_tool = {
    "type": "function",
    "name": "vacation_planner",
    "description": "Plan a vacation based on the given parameters.",
    "parameters":{
        "type":"object",
        "properties":{
            "latitude":{
                "type": "number",
                "description":"The latitude of the destination",
            },
            "longitude":{
                "type": "number", "description":"The longitue of the destination"
            },
            "destination":{
                "type":"string",
                "description": "The destination for the vacation."
            },
            "start_date":{
                "type":"string",
                "description": "The start date of the vacation in YYYY-MM-DD format."
            },
            "end_date":{
                "type":"string",
                "description": "The end date of the vacation in YYYY-MM-DD format."
            },
            "budget":{
                "type":"number",
                "description": "The budget for the vacation."
            }
        },
        "required": ["destination", "start_date", "end_date", "budget"]
    }
}


def chat_with_gemini(prompt):
    history.append({
        "type": "user_input",
        "content": [{"type": "text", "text": prompt}]

    })
    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        store=False,
        input=history,
        tools=[weather_tool, currency_converter_tool, web_search_tool, create_note_tool, list_files_tool, read_file_tool, create_file_tool, get_cryptocurrency_rate_tool, get_flight_info_tool, vacation_planner_tool]
       
    )
    return interaction


def continue_interaction():
    return client.interactions.create(
        model="gemini-3.6-flash",
        store=False,
        input=history,
        tools=[weather_tool, currency_converter_tool, web_search_tool, create_note_tool, list_files_tool, read_file_tool, create_file_tool, get_cryptocurrency_rate_tool, get_flight_info_tool, vacation_planner_tool]
    )

available_functions = {"get_weather": get_weather, "get_exchange_rates": get_exchange_rates, "search": search, "create_note": create_note, "list_files": list_files, "read_file": read_file, "create_file": create_file, "get_cryptocurrency_rate": get_cryptocurrency_rate, "get_flight_info": get_flight_info, "vacation_planner": vacation_planner}

file_creation_tools = {"create_file", "create_note"}

def confirm_file_creation(tool_name, arguments):
    path = "notes.txt" if tool_name == "create_note" else arguments.get("path", "<unspecified>")
    content = arguments.get("content", arguments.get("note", ""))
    preview = content[:500]
    if len(content) > 500:
        preview += "..."

    print(f"The agent wants to create or update: {path}")
    if preview:
        print(f"Content preview:\n{preview}")
    return input("Allow this file operation? [y/N] ").strip().lower() in {"y", "yes"}

def main():
    print("Welcome to Gemini Chat! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting Gemini Chat. Goodbye!")
            break
        interaction = chat_with_gemini(user_input)
        print("Gemini is thinking...")

        while True:
            function_call_handled = False
            for step in interaction.steps:
                history.append(step.model_dump())
                print(f"Step type: {step.type}", f"Step name: {getattr(step, 'name', 'N/A')}", f"Step arguments: {getattr(step, 'arguments', 'N/A')}", f"Step content: {getattr(step, 'content', 'N/A')}", sep="\n")
                if step.type == 'function_call':
                    function_call_handled = True
                    print("Gemini is calling a function:", step.name)
                    if step.name in file_creation_tools and not confirm_file_creation(step.name, step.arguments):
                        result = {
                            "status": "denied",
                            "message": f"User denied permission to create or update {step.arguments.get('path', 'notes.txt')}."
                        }
                    else:
                        result = available_functions[step.name](**step.arguments)
                    print(f"Called {step.name}({step.arguments}) -> {result}")
                    history.append({
                        "type": "function_result",
                        "call_id": step.id,
                        "name": step.name,
                        "result": [{"type": "text", "text": json.dumps(result)}]
                    })
                    interaction = continue_interaction()
                    break

                if step.type == "model_output":
                    text = "".join(
                        part.text
                        for part in step.content
                        if getattr(part, "type", None) == "text"
                    )
                    print("Gemini:", text)

            if not function_call_handled:
                break

if __name__ == "__main__":
    main()