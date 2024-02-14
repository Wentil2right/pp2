import datetime

def drop(dt):
    return dt.replace(microsecond = 0)
x = datetime.datetime.now()
without = drop(x)
print(x)
print(without)