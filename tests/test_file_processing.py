import unittest
import json
import os
import pandas as pd
from datetime import datetime
from ai_commons.file_processing.excel_parser import ExcelConverter
from ai_commons.file_processing.json_validator import remove_keys_from_json, change_timestamp_format

class TestExcelConverter(unittest.TestCase):
    
    def setUp(self):
        # 创建一个测试的DataFrame
        self.data = {
            'Timestamp': [pd.Timestamp('2024-04-20 22:03:30'), pd.Timestamp('2024-04-10 22:49:39')],
            'Account': ['ABC123', 'XYZ789'],
            'Holdback': ['None', 'Test holdback message'],
            'Comments': [None, None],
            'Features': [None, None]
        }
        self.df = pd.DataFrame(self.data)
        
        # 保存为Excel文件
        self.test_excel_file = 'test_excel_file.xlsx'
        self.df.to_excel(self.test_excel_file, index=False, engine='openpyxl')
        
    def tearDown(self):
        # 删除测试文件
        if os.path.exists(self.test_excel_file):
            os.remove(self.test_excel_file)

    def test_excel_to_json(self):
        # 测试Excel转换为JSON
        converter = ExcelConverter(self.test_excel_file)
        json_string_list = converter.to_json(chunk_size=2)
        
        self.assertEqual(len(json_string_list), 1)
        json_data = json.loads(json_string_list[0])
        
        self.assertEqual(len(json_data), 2)
        self.assertEqual(json_data[0]['Account'], 'ABC123')
        self.assertEqual(json_data[1]['Account'], 'XYZ789')
        self.assertEqual(json_data[0]['Timestamp'], '2024-04-20 22:03:30')

class TestJsonValidator(unittest.TestCase):
    
    def setUp(self):
        self.json_string = '''
        [
            {"Timestamp": "2024-04-20 22:03:30", "Account": "ABC123", "Holdback": "None", "Comments": null, "Features": null},
            {"Timestamp": "2024-04-10 22:49:39", "Account": "XYZ789", "Holdback": "Test holdback message", "Comments": null, "Features": null}
        ]
        '''
    
    def test_remove_keys_from_json(self):
        keys_to_remove = [["Comments"], ["Features"]]
        cleaned_json_string = remove_keys_from_json(self.json_string, keys_to_remove)
        cleaned_data = json.loads(cleaned_json_string)
        
        for item in cleaned_data:
            self.assertNotIn("Comments", item)
            self.assertNotIn("Features", item)
    
    def test_change_timestamp_format(self):
        new_json_string = change_timestamp_format(self.json_string, "Timestamp")
        new_data = json.loads(new_json_string)
        
        self.assertEqual(new_data[0]['Timestamp'], '2024-04-20')
        self.assertEqual(new_data[1]['Timestamp'], '2024-04-10')

if __name__ == '__main__':
    unittest.main()
