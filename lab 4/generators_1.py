n = int(input())
squares = (i**2 for i in range(0, n))
for i in squares:
    if i > n:
        break
    else:
        print(i)