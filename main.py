import re

def game_start():
    incorrect_input = True
    while(incorrect_input is True):
        upper_bound = input("Please enter an upper range for the guessing game: ")
        incorrect_input = check_user_input(upper_bound)

def check_user_input(user_input):
    x = re.findall("^[+]?[0-9]+$",user_input)
    if len(x) == 0:
        print("Incorrect input. Please choose a number not: {}".format(user_input))
        print()
        return True
    else:
        print("Let the games begin")
        return False

if __name__ == '__main__':
    game_start()

