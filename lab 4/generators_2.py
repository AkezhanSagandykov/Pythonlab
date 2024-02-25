n = int(input())
evens = (i for i in range(0, n))
for i in evens:
    if i % 2 == 0:
        print(i)
