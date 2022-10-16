import random

# Change the range via here

random_num = random.randint(0, 10)

attempts = 5

result = ""

while attempts != -1:
    user_guess = int(input("\nEnter the guessed number(0-10):"))

    if user_guess == random_num:
        result = "\nCongratulations, You have won the game..!🥳🥳\n"
        break
    else:
        if attempts == 0:
            result = "\nYou have lost the game..!🙄🙄\n"
            break
        else:
            if user_guess > random_num:
                print(f"\nYou answer {user_guess} is greater.")
            elif user_guess < random_num:
                print(f"\nYou answer {user_guess} is smaller.")
            print(f'\nTry Again, Remaining attempts:{attempts}')
            attempts -= 1
            continue
print(result)
