
# digits = [1, 3, 9, 9]
# digits_str = ''.join(map(str, digits))  # 将列表中的每个数字转换为字符串并连接起来
# digits1 = int(digits_str)  # 将连接后的字符串转换为整数
# digits1 += 1  # 对整数进行加法操作
# lst1 = str(digits1)  # 将结果转换为字符串
# lst2 = list(lst1)  # 将字符串转换为列表
# print(lst2)  # 输出转换为列表的结果


# 定义每个组的字典
a = {9: 'ge'}
b = {9: 'shi'}
c = {9: 'bai'}
d = {9: 'qian'}

# 定义一个函数来处理每个字典的加一操作
def increment_key(dictionary):
    # 将键和值分别取出
    key, value = next(iter(dictionary.items()))
    # 对键进行加一操作，并处理进位
    new_key = (key + 1) % 10
    # 如果加一后的键是0，说明已经进位，需要更新字典结构
    if new_key == 0:
        # 创建一个新的键值对，新键为1，值为原字典
        new_dict = {1: dictionary}
    else:
        # 否则，直接更新当前字典的键
        new_dict = {new_key: value}
    return new_dict

# 对每个字典进行加一操作
a = increment_key(a)
b = increment_key(b)
c = increment_key(c)
d = increment_key(d)

# 打印结果
print(a, b, c, d)

