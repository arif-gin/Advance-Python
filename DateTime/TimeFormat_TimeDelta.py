from datetime import timedelta,date,datetime

td=timedelta(days=10)
d=date.today()
print(d+td)

#formating data time
dt=datetime.today()
fdt=dt.strftime("%B,%d,%Y")
print(fdt)

fdt1=dt.strftime("%d-%m-%Y")
print(fdt1)
