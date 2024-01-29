fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
fruits.add("orange")
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
fruits.remove("banana")
fruits.discard("banana")