import re
x = input()
words = re.findall(r'[A-Z][^A-Z]*', x)
spaced = ' '.join(words)
print(spaced)