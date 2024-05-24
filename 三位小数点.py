
num = float(input("请输入一个浮点数: "))

# 将浮点数转换为字符串，以便后续处理
num_str = str(num)

# 检查浮点数是否有小数点，并获取小数部分
if '.' in num_str:
    decimal_part = num_str.split('.')[1]
    # 如果小数部分长度大于3，则只保留三位小数
    if len(decimal_part) > 3:
        rounded_num = round(num, 3)
        print("保留3位小数后的数字是:", rounded_num)
    else:
        # 小数部分长度没有超过3位，直接输出
        print("原始数字是:", num)
else:
    # 如果没有小数点，则直接输出整数
    print("原始数字是:", num)