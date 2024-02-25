n = int(input())
downwards = (i for i in range(n, -1, -1))
for i in downwards:
    print(i)