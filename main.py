# 获取Python保留字列表
import keyword

def convert_source_file(input_path, output_path):
    # 读取原文件内容
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    converted = []
    # 按单词拆分内容（处理保留字判断）
    words = content.split()
    for word in words:
        # 判断是否为保留字：是则保留原大小写，否则转大写
        if keyword.iskeyword(word):
            converted.append(word)
        else:
            converted.append(word.upper())
    
    # 将处理后的单词拼接回内容（保留原空格分隔）
    converted_content = ' '.join(converted)
    
    # 写入新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

# 执行转换：读取random_int.py，输出到converted_random_int.py
if __name__ == "__main__":
    convert_source_file('random_int.py', 'converted_random_int.py')
