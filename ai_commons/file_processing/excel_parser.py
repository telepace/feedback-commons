# Excel parser module
import pandas as pd
import json
import os

class ExcelConverter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_frame = pd.read_excel(file_path, engine='openpyxl')

    def to_json(self, chunk_size=5):
        json_list = []
        for index, row in self.data_frame.iterrows():
            row_dict = row.to_dict()
            for key, value in row_dict.items():
                if isinstance(value, pd.Timestamp):
                    row_dict[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            json_list.append(row_dict)
        
        chunked_list = [json_list[i:i + chunk_size] for i in range(0, len(json_list), chunk_size)]
        json_string_list = [json.dumps(chunk, ensure_ascii=False) for chunk in chunked_list]
        return json_string_list

    # TODO: Implement to_yaml method
    # def to_yaml(self):
    #     data = self.data_frame.to_dict(orient='records')
    #     return yaml.dump(data, allow_unicode=True)

    # TODO: Implement to_xml method
    # def to_xml(self):
    #     root = ET.Element("root")
    #     for _, row in self.data_frame.iterrows():
    #         item = ET.SubElement(root, "item")
    #         for key, value in row.items():
    #             if isinstance(value, pd.Timestamp):
    #                 value = value.strftime('%Y-%m-%d %H:%M:%S')
    #             child = ET.SubElement(item, key)
    #             child.text = str(value)
    #     return ET.tostring(root, encoding='unicode')
