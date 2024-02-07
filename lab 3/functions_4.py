my_list = list(map(int, input().split()))
prime_list = []
i = 0
def filter_prime(n):
     if n <= 0 or n == 1:
          return False
     for j in range(2, n):
          if n % j == 0:
              return False
     return True
def loop_list(my_list):
     for i in my_list:
          statement = filter_prime(i)
          if (statement == True):
               prime_list.append(i)
     return prime_list
print(loop_list(my_list))