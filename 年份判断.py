s = eval(input('输入年份'))
if (s%4==0 and s%100!=0) or s%400==0:
    print(s,'是闰年')
else:
    print(s,"平年")