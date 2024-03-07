import re
x = input()
words = re.split(r"(?=[A-Z])", x)
print(words)
