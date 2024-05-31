import calendar  # 导入 Python 标准库中的 calendar 模块

# 定义年份和月份
theyear = 2021
themonth = 11

# 使用 calendar 模块的 month 函数来获取月历字符串
thismonth = calendar.month(theyear, themonth, w=0, l=0)

# 打印月历
print(thismonth)

# 使用 prmonth 函数打印月历到控制台
calendar.prmonth(theyear, themonth)