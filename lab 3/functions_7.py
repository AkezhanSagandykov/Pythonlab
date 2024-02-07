my_list = list(map(int, input().split()))
list_007 = []
def spy_game(my_list):
    for i in my_list:
        if i == 0:
            list_007.append(str(i))
        if i == 7:
            list_007.append(str(i))
    new_str = ''.join(list_007)
    print('007' in new_str)
spy_game(my_list)