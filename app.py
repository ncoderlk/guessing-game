import random

# Change the range via here

random_num = random.randint(0, 10)

attempts = 5

result = ""

while attempts != -1:
    user_guess = int(input("\nEnter the guessed number(0-10):"))

    if user_guess == random_num:
        result = "\nCongratulations, You have won the game !\n"
        break
    else:
        if attempts == 0:
            result = "\nYou have lost the game\n"
            break
        else:
            print(f'\nTry Again, {attempts} attempt left..!')
            attempts -= 1
            continue
print(result)
