from itertools import permutations
string = input()
def permu(string):
    arr = permutations(string)
    for i in arr:
        print(''.join(i))
permu(string)