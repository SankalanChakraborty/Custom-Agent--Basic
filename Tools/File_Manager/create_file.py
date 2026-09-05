
def create_file(path, content=""):
    """
    Create a new file at the specified path with optional content.
    
    :param path: The path where the file will be created.
    :param content: The content to write to the file (default is empty).
    :return: A message indicating success or failure.
    """
    try:
        # Create the file and write content to it
        with open(path, 'w') as file:
            file.write(content)
        return f"File created successfully at {path}."
    except FileNotFoundError:
        return f"The directory for the path {path} does not exist."
    except PermissionError:
        return f"Permission denied to create a file at {path}."
    except Exception as e:
        return f"An error occurred while creating the file: {e}"