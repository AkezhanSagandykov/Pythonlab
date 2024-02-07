a = input()
def ispalindrome():
    reverse_string = a[::-1]
    if a == reverse_string:
        return True
    else:
        return False
print(ispalindrome())