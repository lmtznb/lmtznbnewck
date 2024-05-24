
# a=90
# b=5
# if a ==3:
#     print("yes")
#     if b == 5:
#         print('b is 5')
# else:
#     print("no")
#     if b == 5:
#         print('b is 5')
# a=''
# b=3
# if a or b:
#     print('true')
# else:
#     print('a')
# score =input('输入成绩')
# match score:
#     case 'A':
#         print('优秀')
#     case 'B':
#         print("良好")
# for i in 'hello':
#     print(i)
# for i in range(1,11):
#     if i%2==0:
#         print(i)
# i=1
# while i<10:
#     i+=1
#     print(i)
# i=1
# while i<10:
#     #Todo:后续实现
#     print('todo:项目功能')
#     pass
# 1111111111111111111111111111111
# s = "helloworld"
# for i in range(0, len(s)):
#     print(i, s[i], end='\t\t')
#
# print('\n'+'-'*40)
# for i in range(-10, 0):
#     print(i, s[i], end='\t')
# s1 = s[0:5:2]
# print(s1)
# print(s[:5:1])
# print(s[0:7:1])
# print(s[0:6:])
# print(s[::])
# print('*'*10)
# print(s[::-1])
# print(s[-1:-11:-1])
# print("-"*40)
# print(s[0:10:-1])
# print('-'*40)
# print(s[4:-11:-1])
# print('e在s中存在吗？', 'e' in s)
# print('v在s中存在吗？', 'v' in s)
# print("e在s中不存在吗？", 'e' not in s)
# print("v在s中不存在吗？", 'v' not in s)
# print('len():', len(s))
# print('max()', max(s))
# print('min()', min(s))
# print('s.index(o):', s.index('o'))
# print('s.count(l)', s.count('l'))
# lst = ['hello', 'world', 98, 100.5]
# print(lst)
# lst2 = list('helloworld')
# lst3 = list(range(1, 10, 2))
# print(lst2)
# print(lst3)
# print(lst+lst2+lst3)
# print(lst*3)
# print(len(lst))
# print(max(lst3))
# print(min(lst3))
# print(lst2.count('o'))
# print(lst2.index('o'))
# lst4 = [10, 20, 30]
# print(lst4)
# # del lst4
# print(lst4)
# lst = ['hello', 'world', 'python', 'php']
# for item in lst:
#     print(item)
# for i in range(0, len(lst)):
#     print(i, '-->', lst[i])
# for index,item in enumerate(lst):
#     print(index, item)
# for index, item in enumerate(lst,start=1):
#     print(index, item)
# for index, item in enumerate(lst,1):
#     print(index, item)
lst = ['hello', 'world', 'python']
print('原列表', lst, id(lst))
lst.append('sql')
print('增加元素之后：', lst, id(lst))
lst.insert(1, 100)
print(lst)
lst.remove('world')
print('删除元素之后的列表', list, id(lst))
print(lst.pop(1))
print(lst)
lst.reverse()
print(lst)
new_lst = lst.copy()
print(lst, id(lst))
print(new_lst, id(new_lst))
lst[1] = 'mysql'
print(lst)
lst = [4, 56, 3, 78, 40, 50, 89]
print('原列表', lst)
lst.sort()
print('升序', lst)
lst.sort(reverse=True)
print('降序', lst)
lst2 = ['banana', 'Apple', 'Cat', 'Orange']
print('原列表', lst2)
lst.sort()
print('升序', lst2)
lst2.sort(reverse=True)
print('降序', lst2)
lst2.sort(key=str.lower)
print(lst2)
import random
lst = [item for item in range(1, 11)]
print(lst)
lst = [item*item for item in range(1, 11)]
print(lst)
lst = [random.randint(1, 100) for _ in range(10)]
print(lst)
lst = [i for i in range(10) if i % 2 == 0]
print(lst)
lst = [
    ['城市', '环比', '同比'],
    ['北京', 102, 103],
    ['上海', 104, 504],
    ['深圳', 100, 39]
]
print(lst)
for row in lst:
    for item in row:
        print(item, end='\t')
    print()
lst2 = [[j for j in range(5)]for i in range(4)]
print(lst2)
