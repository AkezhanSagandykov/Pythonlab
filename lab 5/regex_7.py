import re
def snakeToCamel(x):
    words = x.split('_')
    CamelString= words[0]
    for char in words[1:]:
        CamelString += char.capitalize()
    return CamelString
x = input()
print(snakeToCamel(x))