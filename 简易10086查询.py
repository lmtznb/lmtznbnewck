print("10086查询功能")
print('1查询余额')
print('2查询流量')
print('3查询通话')
print('0退出功能')

x = 1

while x != 0:
    x = eval(input('输入数字进行查询:'))
    if x == 1:
        print('当前余额为100元')
        continue
    if x==2:
        print('当前剩余流量为','G')
        continue
    if x==3:
        print('当前剩余通话为','分钟')
        continue
    if x==0:
        print('正在退出查询系统')
        break
    else:
        print('输入错误无法查询')
        continue

