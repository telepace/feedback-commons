# Json validator module

import json
from datetime import datetime

def remove_keys_from_json(json_string, keys_to_remove):
    # 解析JSON字符串为列表
    data_list = json.loads(json_string)
    
    # 遍历列表中的每个字典
    for data in data_list:
        for key_list in keys_to_remove:
            for key in key_list:
                if key in data:
                    del data[key]
    
    # 将列表转换回JSON字符串
    return json.dumps(data_list, ensure_ascii=False)

import json
from datetime import datetime

def change_timestamp_format(json_string, timestamp_field):
    """
    将JSON字符串中的指定字段的时间戳格式从 'YYYY-MM-DD HH:MM:SS' 改为 'YYYY-MM-DD'。

    Args:
    json_string (str): 输入的JSON字符串。
    timestamp_field (str): 需要转换时间戳格式的字段名。

    Returns:
    str: 修改后的JSON字符串。
    """
    data_list = json.loads(json_string)
    
    for data in data_list:
        if timestamp_field in data:
            try:
                original_timestamp = data[timestamp_field]
                new_timestamp = datetime.strptime(original_timestamp, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
                data[timestamp_field] = new_timestamp
            except ValueError:
                pass
    
    return json.dumps(data_list, ensure_ascii=False)
