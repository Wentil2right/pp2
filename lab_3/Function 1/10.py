def unique(arr):
    result = []
    for element in arr:
        if element not in result:
            result.append(element)
         
    return result
                



n = int(input("n:"))
arr = []
for i in range(n):
    a = int(input("a:"))
    arr.append(a)    

new = unique(arr)
print(new)
    