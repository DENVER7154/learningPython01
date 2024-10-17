import random

answer=random.randint(0,100)
def guessCheck(num):
    while num!=answer:
        if num>answer:
            print("Too high, try again")
        else:
            print("Too low, try again")
        guess=int(input(""))
        guessCheck(guess)  
    print("You guessed the right number, it was",answer)
print("enter a number between 1 and 100")
guess=int(input(""))
guessCheck(guess)
