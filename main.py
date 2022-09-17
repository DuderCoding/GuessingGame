import re

def game_start():
    upper_bound = input("Please enter an upper range for the guessing game: ")
    x = re.findall("^[+]?[0-9]+$",upper_bound)

    if len(x) == 0:
        print("Incorrect input")
    else:
        print("Let the games begin")

if __name__ == '__main__':
    game_start()

