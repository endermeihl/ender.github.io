import requests

def create_job_request(device_type, operation_type, virtual_number):
    url = 'https://service.aciga.com.cn/IoT/smart-control/job/createJob'
    
    headers = {
        'Host': 'service.aciga.com.cn',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'traceId': 'ACIGA2334AF717347246828D85828971377FBF1729389819000097',
        'User-Agent': 'iPhone15,2(iOS/18.0.1) WeexGroup(',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VUeXBlIjoiUEhPTkVfSU9TIiwiY2xpZW50SWQiOiIxZjk5YjJlMzNlYTU0MTAyOTBlZGZjYjY3YjI3ZTA1ZCIsImN1c3RvbWVyTmFtZSI6IueUqOaItzI1NTciLCJjbGllbnRfaWQiOiIxZjk5YjJlMzNlYTU0MTAyOTBlZGZjYjY3YjI3ZTA1ZCIsImN1c3RvbWVyT2xkSWQiOjEzNDQzNDQ3LCJjdXN0b21lclBob25lIjoiMTg2MDE0ODI1NTciLCJzY29wZSI6WyJhbGwiXSwiY3VzdG9tZXJJZCI6IjkwNTAyODE0NTUwNDE5MDQ5MSIsInRlbmFudElkIjoiNWI1OWEyYTQyYjAxNDM1NTgyZWIzZjk1MDQ4N2UyMmYiLCJleHAiOjE3MzE5ODE3OTEsImFwcGxpY2F0aW9uSWQiOjE0LCJncmFudFR5cGUiOiJvYXV0aDJfc21zIiwianRpIjoiYTEyNzg1Y2ItYTY3My00NDQzLTliZTUtYmU3MTAzMzFmYzJhIn0.iBeRE7VGLtHdmNFrgZrC6jXoVla7pTuRYP6O5gYlL44',
        'Content-Length': '210',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
    }
    
    # 构造请求体
    data = {
        "desc": "test",
        "jobDocument": operation_type,  # 传入的操作类型结构体
        "type": device_type,  # 传入的设备类型
        "timeoutConfig": {
            "inProgressTimeoutInSeconds": 0,
            "num": 0
        },
        "virtualNumber": virtual_number  # 传入的设备ID
    }
    
    # 发送请求
    response = requests.post(url, headers=headers, json=data)
    
    # 输出响应内容
    print(f"Status Code: {response.status_code}")
    
    try:
        print(f"Response JSON: {response.json()}")
    except ValueError:
        print("Response is not in JSON format.")

# 示例调用
device_type = "INVOKE_SERVICE"
operation_type = {
    "inputData": {
        "opt_means": "open"
    },
    "serviceCode": "curtain_opt"
}
virtual_number = "94DEB8FFFE2D5923-1"

create_job_request(device_type, operation_type, virtual_number)
