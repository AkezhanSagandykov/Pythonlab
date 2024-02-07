a = input()
def reversed_string():
    new_list = a.split()
    new_list = sorted(new_list, reverse = True)
    for i in new_list:
        print(i, end=' ')
reversed_string()