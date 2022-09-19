import re
import random

def game_start():
    incorrect_input = True
    while incorrect_input is True:
        upper_bound = input("Please enter an upper range for the guessing game: ")
        incorrect_input = check_user_input(upper_bound)
        print()
    upper_bound = upper_bound.lstrip("0")
    print("Let the games begin...\nI am thinking of a number between 1 and {}. Can you guess what it is? ".format(upper_bound))
    computers_number = random.randint(1, int(upper_bound))
    print(computers_number)
    computer_hints = hints(computers_number)
    user_guesses(computers_number, computer_hints, upper_bound)

def check_user_input(user_input):
    x = re.findall("^[+]?([1-9]&|[0-9])+$",user_input)
    if len(x) == 0 or user_input == "0":
        print("Incorrect input. Please choose a number greater than 0, not: {}".format(user_input))
        return True
    else:
        return False

def hints(number):
    #Here, we find hints to give the user based off the random number generated.
    hints_array = []
    if number % 2 == 0:
        hints_array.append("Even")
    else:
        hints_array.append("Odd")
    if number > 30:
        if number % 3 == 0:
            hints_array.append("Multiple of 3")
        if number % 4 == 0:
            hints_array.append("Multiple of 4")
        if number % 5 == 0:
            hints_array.append("Multiple of 5")
    return hints_array

def user_guesses(computers_number,computer_hints, upper_limit):
    current_round = 1
    number_of_fixed_hints = len(computer_hints)
    continue_game = True
    incorrect_input = True
    player_guess = [0]
    all_fixed_hints_given = False
    while continue_game is True:
        if not all_fixed_hints_given:
            if current_round-1 < number_of_fixed_hints:
                if current_round-1 == 0:
                    print("Hint: The number you are guessing is an {} number".format(computer_hints[0]))
                else:
                    print("Hint: The number you are guessing is divisible by {}".format(computer_hints[current_round-1]))
            if current_round == number_of_fixed_hints:
                all_fixed_hints_given = True
        else:
            if player_guess[current_round - 1] < computers_number:
                print("Hint: You need to guess higher!\n")
            elif player_guess[current_round - 1] > computers_number:
                print("Hint: You need to guess lower!\n")

        if computers_number > 100 and current_round > 2:
            old_guess = player_guess[current_round - 2]
            newer_guess = player_guess[current_round - 1]
            if (old_guess - computers_number > 0 and newer_guess - computers_number > 0) and (old_guess - computers_number < newer_guess - computers_number):
                print("Your guess of {} was closer than your newer guess of {}".format(old_guess,newer_guess))
            elif (old_guess - computers_number < 0 and newer_guess - computers_number < 0) and (old_guess - computers_number < newer_guess - computers_number):
                print("Your guess of {} was closer than your older guess of {}".format(newer_guess,old_guess))

        print("------ Round {} ------\n".format(current_round))
        while incorrect_input is True:
            temporary_guess = input("Enter a guess: ")
            incorrect_input = check_user_input(temporary_guess)
            print()
        incorrect_input = True
        player_guess.append(int(temporary_guess))

        if player_guess[current_round] == computers_number:
            print("You got it right. Well done, the game has finished.")
            break
        else:
            current_round = current_round + 1
            print("Nope. Try again!")

if __name__ == '__main__':
    game_start()