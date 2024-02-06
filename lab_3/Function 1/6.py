def reverse(soilem):
    soz = soilem.split()
    reversed_soz = ' '.join(reversed(soz))
    return reversed_soz



user = input(":")
result = reverse(user)
print(result)