import pdb
import os
from sys import platform

# global variable updated by update_dictionary function
running_dictionary = {'1': '', '2': '', '3': '',
                      '4': '', '5': '', '6': '',
                      '7': '', '8': '', '9': ''}


def update_dictionary(player_letter, position):
    """Update running dictionary"""

    global running_dictionary
    position = str(position)
    running_dictionary[position] = str(player_letter)


def clear_screen():
    """Clear command window screen"""

    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


def chose_marker():
    """Chose marker symbol for Player 1 and assign second letter to Player 2
    :returns
    str1 -- Player 1 symbol
    str2 -- Player 2 symbols
    """

    possible_choices = {'X', 'O'}
    player_1_choice = input("Player 1 select a maker; 'X' or 'O': ")
    while player_1_choice.upper() not in possible_choices:
        clear_screen()
        print('Invalid input: Please pick from the given options.')
        player_1_choice = input("Player 1 select a maker; 'X' or 'O': ")
    player_2_default_choice = possible_choices.difference(player_1_choice.upper())
    clear_screen()
    return player_1_choice.upper(), player_2_default_choice.pop()


def dictionary_empty_spots(dictionary):
    """Return a key:value pair dictionary where dictionary value is an empty"""

    return {key: value for key, value in dictionary.items() if value == ''}


def board(dictionary):
    """print out board with spots filled by current running dictionary values"""

    print('{aa:^3} : {ab:^3} : {ac:^3}'.format(aa=dictionary['1'], ab=dictionary['2'], ac=dictionary['3']))
    print('{ba:^3} : {bb:^3} : {bc:^3}'.format(ba=dictionary['4'], bb=dictionary['5'], bc=dictionary['6']))
    print('{ca:^3} : {cb:^3} : {cc:^3}'.format(ca=dictionary['7'], cb=dictionary['8'], cc=dictionary['9']))


def check_winner():
    """check player positions for a winner"""

    player_1_positions = [int(key) for key, value in running_dictionary.items() if value == player_1_marker]
    player_2_positions = [int(key) for key, value in running_dictionary.items() if value == player_2_marker]
    winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
    for combination in winning_combinations:
        if set(combination).issubset(set(player_1_positions)):
            print('Winner: Player 1')
            return 1
        elif set(combination).issubset(set(player_2_positions)):
            print('Winner: Player 2')
            return 1
    # no winner yet
    return 0


def validate_input(player, player_marker):
    """Check validity of input"""

    empty_spots = dictionary_empty_spots(running_dictionary)
    user_input = 'dummy string place holder'

    while not user_input.isdigit() or user_input not in empty_spots:
        user_input = input(f"Player_{player}: Input a cell number of an empty cell on the grid:")

        # input not a digit
        if not user_input.isdigit():
            reset_display()
            print(f"\n Invalid input: Input must be an integer between 1 - {len(running_dictionary)} \n")
            continue

        # input a digit valid and proposed position empty
        elif user_input.isdigit() and user_input in empty_spots:
            update_dictionary(player_letter=player_marker, position=int(user_input))
            reset_display()

        # input a digit valid but proposed position is not
        elif user_input.isdigit() and user_input not in empty_spots:
            reset_display()
            print(f"\n Invalid input: Input cell must be empty: {[int(num) for num in empty_spots.keys()]} \n")
            continue


def reset_display():
    """reset screen and display current player input and or error message"""
    clear_screen()
    board(running_dictionary)


def player_input(player):
    if player == 1:
        player_marker = player_1_marker
    else:
        player_marker = player_2_marker

    validate_input(player, player_marker)


def play():
    """play tic toc toe game"""

    board(running_dictionary)
    for i in range(2):
        player_input(1)
        player_input(2)

    done = False
    spots_left = 5
    while not done and spots_left >= 1:
        player_input(1)
        done = check_winner()
        spots_left -= 1
        if not done and spots_left >= 1:
            player_input(2)
            done = check_winner()
            spots_left -= 1

            # still no winner: rerun while loop
            if not done or spots_left >= 1:
                continue
            # still no winner  but no more spots left: exit while loop
            elif not done and spots_left < 1:
                print('Winner: None')
                break
            # there is a winner but some boxes are still empty: exit while loop
            elif done and spots_left >= 1:
                break
        # there is no winner and no more spots: exit while loop
        elif not done and spots_left < 1:
            print('Winner: None')
            break


# run script
clear_screen()

player_1_marker, player_2_marker = chose_marker()

play()
