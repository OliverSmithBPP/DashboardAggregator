import json

def write_data_to_json(file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)