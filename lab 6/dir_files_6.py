import os
letter = ord('A')-1
for i in range(26):
    letter = letter + 1
    filename = str(chr(letter)) + ".txt"
    with open(filename, 'w') as file:
        file.write(str(letter))