import random
import os
from data import options


# def clear_stdout():
#     os.system('cls' if os.name == 'nt' else 'clear')


def clear_stdout():
    print("\033c", end="")


def print_heading(heading: str):
    clear_stdout()
    print(heading.upper())
    print(len(heading)*"*")


def print_options():
    print_heading("Hints")
    for key, val in options.items():
        print(f'+/-{key} points close to the secret number => {val}')
    print("\nYour task is to find the secret number.\n"
          "To make your search easier use the given hints.")


def print_invalid_input(flag: bool, num, rand_num: int) -> bool:
    if not flag:
        if abs(num - rand_num) <= 5:
            print('Very hot')
        elif abs(num - rand_num) <= 10:
            print('Hot')
        elif abs(num - rand_num) <= 20:
            print('Warm')
        elif abs(num - rand_num) <= 30:
            print('Cold')
        elif abs(num - rand_num) <= 40:
            print('Very cold')
        elif abs(num - rand_num) > 40 and num in range(1, 101):
            print('Too much cold...')
    return True


def main():
    rand_num = random.randint(1, 100)
    print_options()
    valid_input = True
    while True:
        # print(rand_num)
        try:
            n = int(input('Enter a number from 1 to 100 or type 0 to exit the game >> '))
        except ValueError:
            print("Please, enter a number >>")
            continue
        if n == 0:
            print("Exit. Come back soon :)")
            break
        elif n == rand_num:
            print("BINGO! YOU WON!")
            break
        elif n > 100 or n < 0:
            print("The number is out of the given range. Enter a number again...")
            continue
        else:
            valid_input = False
        print_options()
        valid_input = print_invalid_input(valid_input, n, rand_num)


if __name__ == '__main__':
    main()
