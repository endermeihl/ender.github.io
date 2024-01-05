import os
import ssl
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.py4e.com/code3/'
path = '/Users/meihailei/Downloads'  # 将此路径替换为您要下载文件的文件夹路径

# 获取网页内容

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
context = ssl.create_default_context()
cafile = os.path.join(os.path.dirname(__file__), 'cacert.pem')
if os.path.exists(cafile):
    context.load_verify_locations(cafile)
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=context) as response:
    html = response.read().decode()

# 解析网页内容，获取所有文件名
soup = BeautifulSoup(html, 'html.parser',from_encoding=response.info().get_param('charset'))
files = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.py') or href.endswith('.txt'):
        files.append(href)


# 下载所有文件
for filename in files:
    file_url = url + filename
    file_path = os.path.join(path, filename)
    req = urllib.request.Request(file_url, headers=headers)
    with urllib.request.urlopen(req, context=context) as response:
        data = response.read()
        with open(file_path, 'wb') as f:
            f.write(data)
    print(f'Downloaded {filename}')