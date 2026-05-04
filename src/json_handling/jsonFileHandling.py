import os
import time
import json


# Timeout for when files are considered too old. Currently set to 300 seconds (5 minutes).
CACHE_TIMEOUT = 300


# Loading the data from the JSON file to display in the HTML page.
def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except OSError as e:
        print(f"Exception occurred while trying to load the json file {file_path}: {e}")


# Writing the data gathered from sources to a JSON file.
def write_data_to_json(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Exception occurred while trying to write to {file_path}: {e}") 


# Checks the age of a file against the timeout (5 minutes). Returns a boolean to indicate if the file is older than the specified time.
def check_file_age(file_path):
    if os.path.isfile(file_path):
        current_time = time.time()
        timestamp = os.path.getmtime(file_path)
        file_age = current_time - timestamp
        if file_age > CACHE_TIMEOUT:
            print(f"File: {file_path} is more than {CACHE_TIMEOUT / 60} minutes old.")
            return True
        else:
            return False    


# Deletes JSON files.
def remove_file(file_path):
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"{file_path} deleted successfully.")
        else:
            print("File does not exist.")
    except OSError as e:
        print(f"Exception occurred while trying to delete file {file_path}: {e}")