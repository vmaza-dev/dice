# AUThOR: Victor Maza
# DATE: 22/6/25
'''
simple program to simulate rolling a dice with dinamic faces
'''

# modules
import random

# functions

def clear_terminal():
    '''
    clear the terminal screen
    '''
    print("\033c", end='')

def roll_die():
    '''Obtain a dice face dinamically'''

    dice_face = [['', '', ''],
                 ['', '', ''],
                 ['', '', '']]

    # define a dictionary whith x positions

    x_positions = {
        1: [(1, 1)],
        2: [(0, 0), (2, 2)],
        3: [(0, 0), (1, 1), (2, 2)],
        4: [(0, 0), (0, 2), (2, 0), (2, 2)],
        5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
        6: [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)],
    }

    die_result = random.randint(1, 6)

    # fill dice_face positions
    # think that I am using tuples for the matrix position
    for row, colummn in x_positions[die_result]:
        dice_face[row][colummn] = 'x'

    return die_result, dice_face


def header():
    '''
    print the header of the program
    '''
    clear_terminal()
    print(r'''
__     __                                  ____             
\ \   / / __ ___   __ _ ______ _          |  _ \  _____   __
 \ \ / / '_ ` _ \ / _` |_  / _` |  _____  | | | |/ _ \ \ / /
  \ V /| | | | | | (_| |/ / (_| | |_____| | |_| |  __/\ V / 
   \_/ |_| |_| |_|\__,_/___\__,_|         |____/ \___| \_/   
''')
    print('-' * 20, 'WELCOME TO ROLLING DICE 1.1 🎲', '-' * 20)
# main program


header()
user_input = input('\nPress enter to roll the die or q to quit: ')
roll = 0
while user_input.lower() != 'q':
    roll += 1
    header()
    
    result, face = roll_die()
    print(f'You roll a {result}!')
    print(f'''
    +-------+                                                  
    | {face[0][0]:<2}{face[0][1]:<2}{face[0][2]:<2}|
    | {face[1][0]:<2}{face[1][1]:<2}{face[1][2]:<2}|
    | {face[2][0]:<2}{face[2][1]:<2}{face[2][2]:<2}|
    +-------+
''')
    print(f'Roll number: {roll}')
    print('-' * 25)
    user_input = input('\nPress enter to roll the die or q to quit: ')


print('Good bye!👋\n')
print('-' * 20, 'END OF THE PROGRAM', '-' * 20)