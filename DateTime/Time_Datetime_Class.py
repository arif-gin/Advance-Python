from datetime import datetime
from datetime import date
from datetime import time

dt=datetime(year=1999,day=31,month=1)
dt1=datetime(1999,1,31)
print(dt)
print(dt1)

ct=datetime.now()
print(ct)
print(ct.day)

cd=date.today()
print(cd)

t=time(hour=15,minute=34,second=12)
print(t)
#t=time(15,35,12)
#print(t.hour)
