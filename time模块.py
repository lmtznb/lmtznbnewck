import time

a = time.time()
for x in range(100000):
     pass
b = time.time() -a
print(b)

print(time.perf_counter())

print(time.perf_counter())
print(time.perf_counter())

#******************************
print(time.gmtime())
#本地时间
print(time.localtime())
a = time.time()
time.localtime(a)

#sleep
print(time.time())
print(time.ctime(time.time()))

#将时间元祖转化为format
a=time.strftime("%Y-%m-%d %X")
print(b)

c = time.strftime("%x %x")
print(c)