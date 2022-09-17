import re
import random
def game_start():
    incorrect_input = True
    while(incorrect_input is True):
        upper_bound = input("Please enter an upper range for the guessing game: ")
        incorrect_input = check_user_input(upper_bound)
        print()
    upper_bound = upper_bound.lstrip("0")
    print("Let the games begin...\nI am thinking of a number between 1 and {}. Can you guess what it is? ".format(upper_bound))
    computers_number = random.randint(1, int(upper_bound))
    print(computers_number)

def check_user_input(user_input):
    x = re.findall("^[+]?([1-9]&|[0-9])+$",user_input)
    if len(x) == 0 or user_input == "0":
        print("Incorrect input. Please choose a number greater than 0, not: {}".format(user_input))
        return True
    else:
        return False

if __name__ == '__main__':
    game_start()