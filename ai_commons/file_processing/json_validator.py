# Json validator module

import json

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