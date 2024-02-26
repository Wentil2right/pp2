import re
a = input("a:")
txt = "ab*"
x = re.search(txt,a)
if x:
    print("Yes, we match")
else: 
    print("No match")
    
    
    
    
