n = int(input())
def get_mod(n):
    j = 0
    for i in range(0, n):
        j += 1
        yield j
result = get_mod(n)
for i in result:
    if i % 3 == 0 or i % 4 == 0:
        print(i)