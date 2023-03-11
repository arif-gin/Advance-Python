from time import time,ctime,localtime

stobj=localtime()

print(stobj.tm_mday,end="/")
print(stobj.tm_mon,end="/")
print(stobj.tm_year)
