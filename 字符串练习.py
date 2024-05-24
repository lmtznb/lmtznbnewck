# name="张三"
# age=20
# a=b=c=d=100  #链式赋值
# a,b,c,d='room' #字符串分解赋值
# print(a)
# print(b)
# print(c)
# print(d)
# print()
# name=input("输入你的姓名")
# age=eval(input('请输入你的年龄'))
# print()
# number=eval(input("输入你的6位中奖号码"))
# if number==987654:
#     print('恭喜你')
# if number!=987654:
#     print("您未中奖")



# if not n%2:
    # print(n,'为偶数')

# a=input("输入一个字符串")
# if a:
 # print("a为非空字符串")
# a=10
# b=5
# if a>b:max=a
# print(max)
score=eval(input('请输入您的成绩'))
if score<0 or score>100:
    print('成绩有误')
elif 0<=score<60:
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')