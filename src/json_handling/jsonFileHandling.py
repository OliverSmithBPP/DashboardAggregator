import os
import time
import json

CACHE_TIMEOUT = 300

def write_data_to_json(file_name, data):
    with open(f"src/{file_name}", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def check_file_age(file_path):
    if os.path.isfile(file_path):
        current_time = time.time()
        timestamp = os.path.getmtime(file_path)
        file_age = current_time - timestamp
        if file_age > CACHE_TIMEOUT:
            print(f"File: {file_path} is more than 5 minutes old.")
            return True
        else:
            return False    


def remove_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"{file_path} deleted successfully.")
    else:
        print("File does not exist.")