from functools import reduce

# 使用reduce函数计算从0到100的整数之和
total = reduce(lambda x, y: x + y, range(101), 0)  # 添加初始值0
print(total)

# 定义一个测试函数，它接受一个函数作为参数并调用它
def test_func(compute):
    result = compute()  # 调用传入的函数
    print(result)

# 传递一个lambda函数给test_func，并在lambda函数中使用sum函数
test_func(lambda: sum(range(101)))