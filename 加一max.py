def add_one(digits):
    # 从后向前遍历列表，进行加法操作
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        # 如果当前位不是10，说明不需要进位，直接返回
        if digits[i] < 10:
            return digits
        # 如果当前位是10，将当前位设置为0，并继续向前一位进位
        digits[i] = 0
    # 如果所有位都加到了10，需要在最前面添加一个1
    return [1] + digits

# 示例输入
digits = [9, 9, 9, 9]
# 调用函数
result = add_one(digits)
# 输出结果
print(result)