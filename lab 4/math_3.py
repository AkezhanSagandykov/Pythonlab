import math
numsides = int(input())
length = float(input())
p = 3.14
tg = math.tan(p / numsides)
ctg = 1 / tg
area = (numsides // 4) * length * length * ctg
print(area)