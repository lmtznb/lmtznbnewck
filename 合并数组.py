num1 = [1, 2, 3, 0, 0]
num2 = [2, 5, 6]
n = 3
m = 3

if 0 <= m and n <= 200 and 1 <= m + n <= 200:
    # 合并两个列表，并使用集合去重
    num3 = list(set(num1) | set(num2))

    # 移除列表中的所有0
    num3 = [x for x in num3 if x != 0]
    num3.sort()
    print('合并后', num3)
    print('升序', num3)


