def format_sentence_to_markdown(sentence, file_name="output.md"):
    screen_width = 80
    text_width = len(sentence)
    
    # 定义框的宽度，确保框比文本宽度大，且至少为20个字符宽
    box_width = max(text_width + 4, 20)
    left_margin = (screen_width - box_width) // 2  # 居中对齐

    # 创建格式化的文本框
    formatted_text = []
    formatted_text.append(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
    formatted_text.append(' ' * left_margin + '| ' + ' ' * (box_width - 4) + ' |')
    
    # 确保句子居中对齐
    sentence_line = sentence.center(box_width - 4)  # 两侧各留 2 个空格的空间
    formatted_text.append(' ' * left_margin + '| ' + sentence_line + ' |')
    
    formatted_text.append(' ' * left_margin + '| ' + ' ' * (box_width - 4) + ' |')
    formatted_text.append(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')

    # 将结果格式化为 Markdown 代码块
    markdown_content = "```\n" + "\n".join(formatted_text) + "\n```"

    # 将内容写入 Markdown 文件
    with open(file_name, 'w') as file:
        file.write(markdown_content)

    print(f"Formatted text written to {file_name}")

# 使用示例
sentence = input("Enter a sentence: ")
format_sentence_to_markdown(sentence)
