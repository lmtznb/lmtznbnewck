def print_postcard(name, address, message):
    # 计算明信片内容的长度
    max_len = max(len(name), len(address), len(message))

    # 打印明信片
    print("*" * (max_len + 4))  # 打印上边界
    print("*" + " " * 2 + name.center(max_len) + " " * 2 + "*")  # 打印名字
    print("*" + " " * 2 + address.center(max_len) + " " * 2 + "*")  # 打印地址
    print("*" + " " * 2 + message.center(max_len) + " " * 2 + "*")  # 打印信息
    print("*" * (max_len + 4))  # 打印下边界


# 输入明信片信息
name = input("请输入您的名字: ")
address = input("请输入您的地址: ")
message = input("请输入您的留言: ")

# 打印明信片
print_postcard(name, address, message)