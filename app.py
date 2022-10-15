import random

print("\nWelcome to Guessing Game\n")


def ask_to_start():
    user_name = input(str("\nHey, Enter your name :"))
    played_users = open("last-user.txt", "w")

    played_users.writelines(user_name)
    played_users.close()

   # Display Menu
    print("MENU\n")
    print("1 : Start Game")
    print("2 : Exit Game \n")

    user_exit_choice = int(input("Enter your choice : "))
    if user_exit_choice == 1:
        ask_for_range(user_name)
    else:
        exit()


def ask_for_range(user_name):
    max_range = int(input("\nEnter the number range: "))
    if max_range != "":
        random_number = random.randint(0, max_range)
        if random_number == max_range:
            random_number = random.randint(0, max_range)
        else:
            check_answer(random_number, user_name)


def check_answer(random_number, user_name):
    user_answer = int(input("\nEnter the guessed number: "))
    if user_answer == random_number:
        print(f"\nCongratulations, You Have Won The Game {user_name}..!\n")
        exit()
    else:
        while user_answer != random_number:
            if (user_answer < random_number):
                print("\nNumber you have entered is too low..!\n")
                print("\nTry again...\n")
                check_answer(random_number, user_name)
            if (user_answer > random_number):
                print("\nNumber you have entered is too high..!\n")
                print("\nTry again...\n")
                check_answer(random_number, user_name)


ask_to_start()
