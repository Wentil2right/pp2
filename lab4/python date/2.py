import datetime

x = datetime.datetime.now()
print(f"Yesterday {x.year,x.month,x.day - 1}")
print(f"Today {x.year,x.month,x.day}")
print(f"Tomorrow {x.year,x.month,x.day}")
