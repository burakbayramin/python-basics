import random
import time

print("Guess number between 1 and 50")
rand_num = random.randint(1, 50)
guess_num = 5

while True:
    guess = int(input("Enter number"))
    
    if(guess_num == 0):
        print("You lose, numbe is", rand_num)
        break
    elif(guess < rand_num):
        print("Processing...")
        time.sleep(1)
        guess_num -= 1
        print("Your guess less than real number, remaining guess", guess_num)
    elif(guess > rand_num):
        print("Processing...")
        time.sleep(1)
        guess_num -= 1
        print("Your guess bigger than real number, remaining guess", guess_num)
    else:
        print("You win")
        