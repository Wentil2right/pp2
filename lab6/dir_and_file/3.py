import os
path = 'C:\\Users\\User\\Desktop\\pp2\\lab6'
if os.path.exists(path):
    print("exist")
    print(os.path.basename)
    print(os.path.dirname)
else:
    print("not exists")