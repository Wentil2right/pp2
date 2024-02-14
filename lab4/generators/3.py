def div3_4(n):
    for i in range(0, n+1):
        if i % 3 == 0 or i % 4 == 0:
            print(i)
 
a =  int(input("n "))          
div3_4(a)