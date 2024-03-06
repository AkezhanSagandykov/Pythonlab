import re
def search_pattern(x):
    p = r'ab{2,3}' 
    if re.match(p, x):
        return True
    else:
        return False
x = input()
print(search_pattern(x))