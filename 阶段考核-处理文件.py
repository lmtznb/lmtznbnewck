# 定义一个函数a，它接受一个名为ips的参数，这个参数应该是一个包含IP地址的列表。
def a(ips):

    # 创建一个空字典data_dict，用来存储每个IP地址及其出现的次数。
    data_dict = {}

    # 遍历ips列表中的每个元素（即每个IP地址）。
    for i in ips:
        # 如果当前IP地址i已经在data_dict字典中，则将其计数增加1。
        if i in data_dict:
            data_dict[i] += 1
        # 如果当前IP地址i不在data_dict字典中，则将其添加到字典中，并设置计数为1。
        else:
            data_dict[i] = 1

    # 对data_dict字典中的项进行排序，按照每个IP地址出现的次数（即字典的值）降序排序。
    sorted_items = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

    # 打印排序后的字典项。
    print(sorted_items)

    # 打开（或创建）一个名为'new.csv'的文件用于写入，文件路径是'../../Downloads/untitled/untitled/'。
    with open('../../Downloads/untitled/untitled/new.csv', 'w') as f:
        # 遍历排序后的字典项。
        for ip, count in sorted_items:
            # 将每个IP地址及其出现次数写入到文件中，格式为"IP:次数"，每条记录占一行。
            f.write(f"{ip}:{count}\n")

# 定义一个变量path，存储攻击日志文件的路径。
path = '../../Downloads/untitled/untitled/attack.csv'

# 读取path指定的文件，并将每一行去除空白字符后作为列表元素存储到ips列表中。
ips = [line.strip() for line in open(path, 'r') if line.strip()]

# 调用函数a，并传入ips列表作为参数。
a(ips)