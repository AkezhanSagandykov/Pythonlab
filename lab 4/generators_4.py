a = int(input())
b = int(input())
def squares_in_between(a, b):
    j = a - 1
    for i in range(a, b + 1):
        j += 1
        yield j
interval = squares_in_between(a, b)
for i in interval:
    print(i * i)