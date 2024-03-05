import os
path = 'C:\\Users\\User\\Desktop\\pp2\\lab6'
if os.path.exists("1.txt"):
    print(os.access("1.txt", os.F_OK))
    os.remove("1.txt")
else:
    print("not exists")
        