import unittest
import os
import json
from json_handling import jsonFileHandling

class TestJsonFileHandling(unittest.TestCase):

    def test_load_json(self):
        fake_data = {"key": "load_test"}
        file_path = "test/resources/load_data_test"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(fake_data, file, indent=2, ensure_ascii=False)
        
        result = jsonFileHandling.load_json(file_path)
        
        assert result == fake_data


    def test_write_data_to_json(self):
        fake_data = {"key": "write_test"}
        file_path = "test/resources/write_data_test"

        jsonFileHandling.write_data_to_json(file_path, fake_data)

        with open(file_path, 'r') as file:
            result = json.load(file)

        assert result == fake_data    


    def test_remove_file(self):
        fake_data = {"key": "remove_test"}
        file_path = "test/resources/remove_data_test"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(fake_data, file, indent=2, ensure_ascii=False)

        jsonFileHandling.remove_file(file_path)

        result = os.path.isfile(file_path)

        assert not result