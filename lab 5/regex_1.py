import re
def pattern(x):
    p = r'ab*' 
    if re.match(p, x):
        return True
    else:
        return False
x = input()
print(pattern(x))