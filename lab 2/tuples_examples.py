mytuple = ("apple", "banana", "cherry")
print(mytuple[1])
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y) #change tuple values
print(x)
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits #unpacking tuple
print(green)
print(yellow)
print(red)
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) #loop tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
