import re
a = input("a:")
txt = "a.*b$" 
x = re.findall(txt,a)
if x:
    print("Yes, we match")
else: 
    print("No match")
    