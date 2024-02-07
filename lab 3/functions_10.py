my_list = list(map(int, input().split()))
unique_list = {}
def unique_array(my_list):
    for i in my_list:
        number = i
        unique_list[number] = number + 1
    return unique_list
temp = unique_array(my_list)
result = []
for i in temp.keys():
    result.append(i)
print(result)