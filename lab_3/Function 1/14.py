import random

def Game():
    Player_name = input("Сіздің атыңыз:")
    print(f"Сәлем,{Player_name} 1 ден 20ға дейінгі сандардың бірін таңдаңыз!")
    
    try_num = 1
    com_num = random.randint(1,20)
    while True:
        your_num = int(input("Сіздің саныңыз:"))
        if com_num > your_num:
            print("Одан көп :( ")
            try_num+=1
        elif com_num < your_num:
            print("Одан аз  :(") 
            try_num+=1
        else:
            print(f"Құттықтаймын сіз {try_num} мүмкіндіктен жеңдіңіз!")
            break
        
        
Game()   
        