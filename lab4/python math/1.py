import math
def deg_red(a):
    ra =float(a*math.pi/180)
    return ra 

x = float(input("Degree:"))
result = deg_red(x)
print(result)
