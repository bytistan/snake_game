import json 

def read_json_file(file_path):
    """
    Reads a JSON file and returns its contents as a Python dictionary.

    Args:
    - file_path (str): The path to the JSON file.

    Returns:
    - dict: The contents of the JSON file as a Python dictionary.
    """
    try:
        with open(file_path) as f:
            data = json.load(f)
            f.close()
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON file '{file_path}'.")
        return None
    

def update_json_file(file_path, updated_data):
    """
    Updates a JSON file with new data.

    Args:
    - file_path (str): The path to the JSON file.
    - updated_data (dict): The updated data to be written to the JSON file.

    Returns:
    - bool: True if the update is successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(updated_data, f, indent=4)
        return True
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False
    except Exception as e:
        print(f"Error: Unable to update JSON file '{file_path}'. {e}")