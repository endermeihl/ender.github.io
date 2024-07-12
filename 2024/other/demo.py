import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup

# 设置Chrome选项
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# 使用ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 打开目标网页
url = "https://www.autohome.com.cn/car/"
driver.get(url)

# 模拟滚动页面加载所有品牌
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # 向下滚动页面
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 等待页面加载
    time.sleep(3)
    # 计算新的滚动高度并与之前的高度进行比较
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 获取页面HTML
page_source = driver.page_source

# 关闭浏览器
driver.quit()

# 解析HTML
soup = BeautifulSoup(page_source, 'html.parser')

# 提取品牌和车型数据
brands = []
models = []

# 查找所有品牌和车型
brand_sections = soup.find_all('dl')
print(f"Found {len(brand_sections)} brand sections")

for section in brand_sections:
    dt = section.find('dt')
    if not dt:
        print(f"No dt found in section: {section}")
        continue

    brand_tag = dt.find('div').find('a')
    if not brand_tag:
        print(f"No a tag found in dt: {dt}")
        continue

    brand_name = brand_tag.text.strip()
    print(f"Processing brand: {brand_name}")

    dd_elements = section.find_all('dd')
    if not dd_elements:
        print(f"No dd elements found for brand: {brand_name}")
        continue

    for dd in dd_elements:
        model_tags = dd.find_all('h4')
        if not model_tags:
            print(f"No h4 tags found in dd: {dd}")
            continue

        for model_tag in model_tags:
            model_link = model_tag.find('a')
            if not model_link:
                print(f"No a tag found in h4: {model_tag}")
                continue

            model_name = model_link.text.strip()
            brands.append(brand_name)
            models.append(model_name)

# 创建DataFrame并修复乱码问题
car_data = pd.DataFrame({
    'Brand': brands,
    'Model': models
})

# 将DataFrame保存为CSV文件，使用UTF-8编码
car_data.to_csv('car_brand_model_data.csv', index=False, encoding='utf-8')

print("Data scraped and saved to car_brand_model_data.csv")

# 显示部分数据以验证
print(car_data.head())