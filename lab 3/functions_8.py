my_list = list(map(int, input().split()))
temp = []
def has_33(nums):
    for i in nums:
        temp.append(str(i))
    list_33 = ''.join(temp)
    return '33' in list_33
print(has_33(my_list))