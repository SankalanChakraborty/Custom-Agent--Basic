import os

# list all files in a given directory

def list_files(directory):
    try:
        # List all files in the directory
        files = os.listdir(directory)
        return {
            "directory": directory, 
            "items": [
                {"name": f, "type": "directory" if os.path.isdir(os.path.join(directory, f)) else "file"}
                for f in files
            ]
        }
    except FileNotFoundError:
        return f"The directory {directory} does not exist."
    except PermissionError:
        return f"Permission denied to access the directory {directory}."


