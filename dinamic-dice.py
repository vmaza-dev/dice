# AUThOR: Victor Maza
# DATE: 19/6/25
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

    die_result = random.randint(1, 6)
    match die_result:
        case 1:
            dice_face[1][1] = 'x'
        case 2:
            dice_face[0][0] = 'x'
            dice_face[2][2] = 'x'
        case 3:
            dice_face[0][0] = 'x'
            dice_face[1][1] = 'x'
            dice_face[2][2] = 'x'
        case 4:
            dice_face[0][0] = 'x'
            dice_face[0][2] = 'x'
            dice_face[2][0] = 'x'
            dice_face[2][2] = 'x'
        case 5:
            dice_face[0][0] = 'x'
            dice_face[0][2] = 'x'
            dice_face[1][1] = 'x'
            dice_face[2][0] = 'x'
            dice_face[2][2] = 'x'
        case 6:
            dice_face[0][0] = 'x'
            dice_face[0][2] = 'x'
            dice_face[1][0] = 'x'
            dice_face[1][2] = 'x'
            dice_face[2][0] = 'x'
            dice_face[2][2] = 'x'                       
    
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
    print('-' * 20, 'WELCOME TO ROLLING DICE 1.0 🎲', '-' * 20)
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
