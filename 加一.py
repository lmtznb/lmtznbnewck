
digits = [1, 3, 9, 9]
digits_str = ''.join(map(str, digits))  # 将列表中的每个数字转换为字符串并连接起来
digits1 = int(digits_str)  # 将连接后的字符串转换为整数
digits1 += 1  # 对整数进行加法操作
lst1 = str(digits1)  # 将结果转换为字符串
lst2 = list(lst1)  # 将字符串转换为列表
print(lst2)  # 输出转换为列表的结果