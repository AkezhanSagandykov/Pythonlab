import re
x = input()
pattern = re.compile(r'a.*b$')
print(pattern.findall(x))