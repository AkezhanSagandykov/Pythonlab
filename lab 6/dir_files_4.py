path = input()
with open(path, 'r') as file:
    s = 0
    for line in file:
        s += 1
    print(s)