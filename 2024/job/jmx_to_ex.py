import xml.etree.ElementTree as ET
import pandas as pd
import json
from collections import defaultdict
import html

def parse_json_params(param_value):
    try:
        # 将 HTML 实体转换为标准 JSON
        json_value = html.unescape(param_value)
        json_value = json.loads(json_value)
        return flatten_json(json_value)
    except json.JSONDecodeError:
        return {param_value: 'String'}

def flatten_json(json_obj, parent_key='', sep='.'):
    items = []
    for k, v in json_obj.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# 读取JMX文件
file_path = '商户自动化.jmx'
tree = ET.parse(file_path)
root = tree.getroot()

# 存储HTTP Sampler的信息
data = defaultdict(list)

for http_sampler in root.iter('HTTPSamplerProxy'):
    sampler_name = http_sampler.get('testname')
    method = None
    url = None
    params = []

    for element in http_sampler.iter('stringProp'):
        if element.get('name') == 'HTTPSampler.method':
            method = element.text
        elif element.get('name') == 'HTTPSampler.path':
            url = element.text

    for element in http_sampler.iter('elementProp'):
        param_value = None
        
        for sub_element in element.iter('stringProp'):
            if sub_element.get('name') == 'Argument.value':
                param_value = sub_element.text

        if param_value:
            # 检查参数值是否为JSON格式并进行解析
            flattened_params = parse_json_params(param_value)
            for key, value in flattened_params.items():
                param_type = type(value).__name__
                params.append({
                    'name': key,
                    'value': value,
                    'type': param_type
                })

    if method and url:
        data[(sampler_name, method, url)].append(params)

# 转换为DataFrame
rows = []
for key, params_list in data.items():
    sampler_name, method, url = key
    for params in params_list:
        param_names = [param['name'] for param in params]
        param_values = [str(param['value']) for param in params]
        param_types = [param['type'] for param in params]

        rows.append({
            'Sampler Name': sampler_name,
            'Method': method,
            'URL': url,
            'Parameter Names': ', '.join(param_names),
            'Parameter Values': ', '.join(param_values),
            'Parameter Types': ', '.join(param_types)
        })

df = pd.DataFrame(rows)

# 保存为Excel文件
output_file = 'output.xlsx'
df.to_excel(output_file, index=False)

print(f"JMX文件已成功解析并转换为Excel文件！文件路径：{output_file}")
