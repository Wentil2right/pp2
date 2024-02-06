def spy_game(nums):
    
    pos_0 = pos_7 = None
    
    for i, num in enumerate(nums):
        if num == 0:
            pos_0 = i
        elif num == 7:
            pos_7 = i
        
        
        if pos_0 is not None and pos_7 is not None and pos_0 < pos_7:
            return True
    
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  