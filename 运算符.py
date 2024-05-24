# x=10
# y=3
# z=x/y
# print(z,type(z))
# print('float类型转成int类型',float(10))
#
# print('float类型转int',int(3.14))
# print('float转int',int(3.9))
# print(int('100')+int('200'))
# # print(int('18a'))
# print(int('3.14'))
# print(ord('杨'))
# print(chr(26472))
# print(hex(26472))
# print(oct(26472))
# print(0b1010)
# s='3.14+3'
# print(s,type(s))
# x=eval(s)
# print(x,type(x))
# age=eval(input('请输入您的年龄'))
# print(age,type(age))
# height=eval(input('请输入您的身高'))
# print(height,type(height))
# hello='北京欢迎你'
# print(hello)
# print(eval('hello'))
# print(eval('北京欢迎你'))
# print('加法',1+1)
# print('减法',1-1)
# print('乘法',2*3)
# print('除法',10/0)
# print('整除',10//3)
# print('取余',10%3)
# print('幂运算',2**4)
x=20
y=10
x=x+y
print(x)
x+=y#40
x-=y#30
print(x)
x*=y
print(x)
x/=y
print(x)
print(type(x))
x%=2
print(x)
z=3
y//=z#y=y//z
print(y)
y**=z
print(y)
a=b=c=100
print(a,b,c)
a,b=10,20
print(a,b)
c,v,v=1,2,3
print(v)
a,b=b,a
print(a,b)
print(98>98,98<98,98==98,98!=98,98>=98,98<=98)
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print(8<7 and 10/0)
print(True or False)
print(not True)
print(not not not (8>7 or 7>8))
print(7>8 and 7>8 or 9<7 and 7<9)
print('按位与运算',12&8)
print('按位或运算',4|8)
print('按位异或运算符',31^22)
print('按位取反',~123)
print('左位移',2<<2)
print('zuo位移',2<<3)
print('右移位',8>>2)
print(-8>>2)

print("abcdefghi")
print(0o362)
print(0xf2)
a,b,c=c,b,a
print()
a&=b