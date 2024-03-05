import os
path = 'C:\\Users\\User\\Desktop\\pp2\\lab 6\\files_A_Z\\files A_Z'

for i in range(26):
    filename = chr(ord('A') + i) + ".txt"
    with open(filename, 'w') as file:
        file.write(f"This is file {filename}\n")
    print(f"File {filename} created.")