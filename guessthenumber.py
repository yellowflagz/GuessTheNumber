# Import random and with the randint function we can generate  
# the random number, in this case between 1 and 20.
import random
secret_num = random.randint(1,20)  
# We ask the user for his name.
print('Hello, what is your name?')
name = input()
print('Hi ' + name + ', i am thinking of a number between 1 and 20.')
# A for loop to iterate as many times as the user has opportunities to guess the number
# Then a simple if conditional to give some hints to the user
for num_guesses in range (1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secret_num:
        print('The number you guessed is too low!')
    elif guess > secret_num:
        print('The number you guessed is too high!')
    else:
        break
# When the user guess the right number or surpasses the guess limit the for loop break
# With another if conditional we let the user know whether if he guessed the right number or not.
if guess == secret_num:
    print('Good job! The number i was thinking of was ' + str(secret_num))
else:
    print('Nope... The number i was thinking of was ' + str(secret_num))







