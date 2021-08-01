import random
secret_num = random.randint(1,20)

print('Hello, what is your name?')
name = input()
print('Hi ' + name + ', i am thinking of a number between 1 and 20.')

for num_guesses in range (1,7):
    print('Take a guess')
    guess = int(input())
    if guess < secret_num:
        print('The number you guessed is too low!')
    elif guess > secret_num:
        print('The number you guessed is too high!')
    else:
        break
if guess == secret_num:
    print('Good job! The number i was thinking of was ' + str(secret_num))
else:
    print('Nope... The number i was thinking of was ' + str(secret_num))







