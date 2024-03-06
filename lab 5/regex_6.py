import re
x = input()
replacedText = re.sub(r'[ ,.]', ':', x)
print(replacedText)