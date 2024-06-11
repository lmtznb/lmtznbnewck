# 初始化计数器
count = 0

# 打开文件并读取
with open('word.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # 将整行转换为小写，以忽略大小写
        line = line.lower()
        # 按空格分割行，得到单词列表
        words = line.split()
        # 统计 "python" 单词出现的次数
        count += words.count('python')

# 打印结果
print(f"The word 'python' appears {count} times in the file.")