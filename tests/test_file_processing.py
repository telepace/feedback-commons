import unittest
import json
import os
import pandas as pd
from ai_commons.file_processing.excel_parser import ExcelConverter
from ai_commons.file_processing.json_validator import remove_keys_from_json

class TestExcelConverter(unittest.TestCase):

    def setUp(self):
        # 创建一个示例Excel文件
        self.test_file = 'test.xlsx'
        df = pd.DataFrame({
            'Timestamp': [pd.Timestamp('2024-04-07 20:50:30'), pd.Timestamp('2024-05-08 15:30:45')],
            'User ID': ['U12345', 'U67890'],
            'Gift': ['Flower', 'Chocolate']
        })
        df.to_excel(self.test_file, index=False)

    def tearDown(self):
        # 删除示例Excel文件
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_to_json(self):
        converter = ExcelConverter(self.test_file)
        json_output = converter.to_json(chunk_size=2)
        expected_output = [
            '[{"Timestamp": "2024-04-07 20:50:30", "User ID": "U12345", "Gift": "Flower"}, {"Timestamp": "2024-05-08 15:30:45", "User ID": "U67890", "Gift": "Chocolate"}]'
        ]
        self.assertEqual(json_output, expected_output)

class TestJsonValidator(unittest.TestCase):

    def test_remove_keys_from_json(self):
        json_string = '[{"Timestamp": "2024-04-07 20:50:30", "User ID": "U12345", "Gift": "Flower"}, {"Timestamp": "2024-05-08 15:30:45", "User ID": "U67890", "Gift": "Chocolate"}]'
        keys_to_remove = [["Timestamp"], ["User ID"]]
        modified_json_string = remove_keys_from_json(json_string, keys_to_remove)
        expected_output = '[{"Gift": "Flower"}, {"Gift": "Chocolate"}]'
        self.assertEqual(modified_json_string, expected_output)

if __name__ == '__main__':
    unittest.main()
