import random
name = input('Hello! What is your name?\n')
greetings = "Well, {} , I am thinking of a number between 1 and 20."
print(greetings.format(name))
number = random.randint(1, 20)
a = int(input('Take a guess.\n'))
i = 1
result = "Good job, {}! You guessed my number in {} guesses!"
if a == number:
    print(result.format(name, 1))
else:
    i += 1
    print("Your guess is too low.")
    while a != number:
        a = int(input('Take a guess.\n'))
        if a != number:
            print('Your guess is too low.')
            i += 1
        else:
            result = "Good job, {}! You guessed my number in {} guesses!"
            break
print(result.format(name, i))