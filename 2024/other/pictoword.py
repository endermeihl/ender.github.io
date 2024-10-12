from pdf2image import convert_from_path
from pytesseract import image_to_string

# 将 PDF 文件转换为图像
images = convert_from_path('sample.pdf', dpi=300)

# 对每页执行 OCR
text = ""
for img in images:
    text += image_to_string(img, lang='eng')

# 保存文字到文件
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
