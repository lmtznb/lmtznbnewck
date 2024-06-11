# f = open('python.txt', 'r', encoding="UTF-8")


f = open('python.txt', 'r', encoding="UTF-8")
lines = f.readlines()

# content = f.readline()
# print(f'第一行：{content}')
# content = f.readline()
# print(f'第er行：{content}')


# 现在lines是一个列表，其中每个元素是文件的一行
f.close()

#for循环1
for line in open("python.txt","r"):
    print(line)


# 打印所有行
# for line in lines:
#     print(line)


# with open('python.txt', 'r', encoding="UTF-8") as f:
#     content = f.readline()
#     print(content)
with open ("python.txt","r") as f:
    f.readline()