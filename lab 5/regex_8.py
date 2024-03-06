import re
x = input()
words = re.findall(r'[A-Z][^A-Z]*', x)
print(words)