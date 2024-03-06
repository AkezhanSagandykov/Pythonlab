import re
x = input()
pattern = re.compile(r"[a-z]+_[a-z]+")
print(pattern.findall(x))