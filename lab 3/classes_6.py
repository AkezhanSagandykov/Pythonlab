my_list = list(map(int, input().split()))
def filter_prime(number):
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
result = list(filter(lambda x : (filter_prime(x) == 1), my_list))
print(result)