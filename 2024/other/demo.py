import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://car.autohome.com.cn/price/brand-33.html#pvareaid=2042362"

# Send a GET request to the webpage
response = requests.get(url)
response.encoding = 'utf-8'  # Ensure correct encoding

# Parse the webpage content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the brand name
brand_name = soup.find('a', href="//car.autohome.com.cn/price/brand-33.html#pvareaid=2042362").text.strip()
print(f"Brand: {brand_name}")

# Find all car models under the brand
models = soup.find_all('li')

for model in models:
    model_name = model.find('h4').text.strip()
    price = model.find('a', class_='red').text.strip() if model.find('a', class_='red') else '暂无'
    detail_url = model.find('h4').find('a')['href']
    detail_url = f"https:{detail_url}"
    
    print(f"Model: {model_name}")
    print(f"Price: {price}")
    print(f"Detail URL: {detail_url}\n")
