import re
a = input("a:")
txt = "[A-Z]{1}[a-z]" 
x = re.search(txt,a)
if x:
    print("Yes, we match")
else: 
    print("No match")