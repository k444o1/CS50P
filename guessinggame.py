import random
import sys
while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            ans = random.randint(1, n)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess > 0 and guess.is_integer():
                        if guess < ans:
                            print("Too small!")
                        elif guess > ans:
                            print("Too large!")
                        else:
                            sys.exit("Just right!")
                except ValueError: #if guess is invalid
                    pass
    except ValueError: #if level is invalid
        pass