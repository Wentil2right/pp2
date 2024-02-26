import re
a = input("a:")
txt = "abb" or "abbb" 
x = re.findall(txt,a)
if x:
    print("Yes, we match")
else: 
    print("No match")
    