def has_33(num):
    my_list = []
    for i in range(num):
        a = int(input("a:"))
        my_list.append(a)
    for i in range(len(my_list) - 1):
        if my_list[i] == 3 and my_list[i + 1] == 3:
            return True
    return False


n = int(input("n:"))   
result = has_33(n)
print(result)