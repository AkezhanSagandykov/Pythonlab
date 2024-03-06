import os
list = []
for i in range(3):
    list.append(input())
with open("words.txt", 'w') as file:
    file.write(str(list))
print(list)