def squares(n):
    for i in range(1,n+1):
        yield i**2
    
    
    
n = int(input("N = "))
result = squares(n)
for i in result:
    print(i)