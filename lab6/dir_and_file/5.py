import os
path = 'C:\\Users\\User\\Desktop\\pp2\\lab6'
name = ['amanay', 'bolat' 'salam','ali']
with open(path, 'w', encoding='utf-8') as file:
    for i in name:
        file.write(i + '\n')
print(path)