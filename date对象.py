from datetime import datetime
a = datetime.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
a=datetime.date(2017,3,1)
b=datetime.date(2017,3,15)
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__lt__(b))
print(a.__ne__(b))



# ******************
print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%y/%m/%d'))
print(a.__format__('%D'))
print(a.__format__('%d'))

# from datetime import _datetime
# a = time(12, 20, 30, 899)
# print(a)

