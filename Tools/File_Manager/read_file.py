def read_file(path):
    try:
        with open(path, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"The file {path} does not exist."
    except PermissionError:
        return f"Permission denied to access the file {path}."