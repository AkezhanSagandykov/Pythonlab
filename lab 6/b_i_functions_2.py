string = input()
l = 0
b = 0
for i in string:
    if i.islower():
        l+=1
    if i.isupper():
        b+=1
print(f"lower letter:{l}")
print(f"upper letters:{b}")