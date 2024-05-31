

from datetime import *
d = date(2012,12,12)
print(d)
d1 =d + timedelta(days=-1)
print(d1)
d2 = d + timedelta(days=1)
print(d2)

dt =datetime(2012,12,12,23,59,59)
print(dt)
dt1 = dt + timedelta(days=-1)
print(dt1)
dt2 = dt + timedelta(days=1)
print(dt2)
dt3 = dt + timedelta(hours=-1)
print(dt3)
dt4 = dt + timedelta(hours=1)
print(dt4)
dt5 = dt + timedelta(seconds=-1)
print(dt5)
dt6 = dt + timedelta(seconds=1)
print(dt6)