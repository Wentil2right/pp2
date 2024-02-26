import re
a = input("a:")
txt = r"[a-z](?:_[a-z])" 
x = re.findall(txt,a)
if x:
    print("Yes, we match")
else: 
    print("No match")
    