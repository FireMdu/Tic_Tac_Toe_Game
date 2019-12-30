import pdb

# global variable updated by update_dictionary function
running_dictionary = {'1': '', '2': '', '3': '',
                      '4': '', '5': '', '6': '',
                      '7': '', '8': '', '9': ''}


def chose_marker():
    """
    Chose marker symbol for Player 1 and assign the the other letter to Player 2
    :returns
    str1 -- Player 1 symbol
    str2 -- Player 2 symbols
    """

    possible_choices = {'X', 'O'}
    player_1_choice = input("Player 1 select a marker or your choice between letters 'X' and 'O': ")
    while player_1_choice.upper() not in possible_choices:
        print('Invalid input: Please chose from the given choices!')
        player_1_choice = input("Player 1 select a marker or your choice between letters 'X' and 'O': ")
    player_2_default_choice = possible_choices.difference(player_1_choice.upper())

    return player_1_choice.upper(), player_2_default_choice.pop()


def update_dictionary(player_letter, position):
    global running_dictionary
    position = str(position)
    running_dictionary[position] = str(player_letter)


def dictionary_empty_spots(dictionary):
    """Return a key:value pair dictionary where value is an empty"""

    return {key: value for key, value in dictionary.items() if value == ''}


def board(dictionary):
    """print out board with spots filled by dictionary values"""

    print('{aa:^3} : {ab:^3} : {ac:^3}'.format(aa=dictionary['1'], ab=dictionary['2'], ac=dictionary['3']))
    print('{ba:^3} : {bb:^3} : {bc:^3}'.format(ba=dictionary['4'], bb=dictionary['5'], bc=dictionary['6']))
    print('{ca:^3} : {cb:^3} : {cc:^3}'.format(ca=dictionary['7'], cb=dictionary['8'], cc=dictionary['9']))


def check_winner():
    """Check player positions for a winner"""

    player_1_positions = [int(key) for key, value in running_dictionary.items() if value == player_1_marker]
    player_2_positions = [int(key) for key, value in running_dictionary.items() if value == player_2_marker]
    winning_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
    for combination in winning_combinations:
        if set(combination).issubset(set(player_1_positions)):
            print('Winner: Congratulations Player 1')
            return 1
        elif set(combination).issubset(set(player_2_positions)):
            print('Winner: Congratulations Player 2')
            return 1
    # no winner yet
    return 0


def ask_player_input(player):
    if player == 1:
        player_marker = player_1_marker
    else:
        player_marker = player_2_marker

    empty_spots = dictionary_empty_spots(running_dictionary)
    # get player input
    player_input = input(f"Player_{player}: Input a cell number for an empty cell on the tic tac toe grid: ")
    while int(player_input) not in range(1, len(running_dictionary) + 1):
        print(f"Invalid input: Input must be an integer between 1 - {len(running_dictionary)}")
        player_input = input(f"Player_{player}: Input a cell number for an empty cell on the tic tac toe grid: ")
    if str(player_input) in empty_spots:
        update_dictionary(player_letter=player_marker, position=int(player_input))


player_1_marker, player_2_marker = chose_marker()

board(running_dictionary)
for i in range(2):
    ask_player_input(1)
    board(running_dictionary)
    ask_player_input(2)
    board(running_dictionary)

no_winner = True
while no_winner:
    ask_player_input(1)
    board(running_dictionary)
    winner = check_winner()
    if not winner:
        ask_player_input(2)
        board(running_dictionary)
        win = check_winner()
        if not win:
            continue
        else:
            break
    else:
        break
