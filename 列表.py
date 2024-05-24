# s = '3.14'
# x = input()
# print(type(x))
# # 排序方法
# numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers.sort()
# print(numbers)  # 输出: [1, 1, 2, 3, 4, 5, 9]
# numbers = [3, 1, 4, 1, 5, 9, 2]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)  # 输出: [1, 1, 2, 3, 4, 5, 9]
# print(numbers)         # 输出: [3, 1, 4, 1, 5, 9, 2]，原始列表未改变
# t = ('hello', [10, 20, 30], 'python', 'word')
# print(t)
# a=tuple('helloword')
# print(a)

# b=tuple([10,20,30,40])
# print(b)
t = ('python', 'hello', 'world')
print(t[0])
t2 = t[0:3:2]
print(t2)
for item in t:
    print(item)
for i in range(len(t)):
    print(i, t[i])
for index,item in enumerate(t):
    print(index, "--->", item)
for index,item in enumerate(t,start=11):
    print(index, "--->", item)
