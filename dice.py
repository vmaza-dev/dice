# AUTOR: Victor Maza
# FECHA: 6/6/25
'''
simple program to simulate rolling a dice
'''

# modules
import random

# functions

def clear_terminal():
    '''
    clear the terminal screen
    '''
    print("\033c", end='')

def roll_die():# obtain the face of the dice after rolling
    die_faces = [
        '''
           +-------+
           |       |
           |   x   |
           |       |
           +-------+''',
        '''
           +-------+
           | x     |
           |       |
           |     x |
           +-------+''',
        '''
           +-------+
           | x     |
           |   x   |
           |     x |
           +-------+''',
        '''
           +-------+
           | x   x |
           |       |
           | x   x |
           +-------+''',
        '''
           +-------+
           | x   x |
           |   x   |
           | x   x |
           +-------+''',
        '''
           +-------+
           | x x x |
           | x x x |
           | x x x |
           +-------+''',
    ]

    die_result = random.randint(1, 6)
    match die_result:
        case 1:
            die_face = die_faces[0]
        case 2:
            die_face = die_faces[1]
        case 3:
            die_face = die_faces[2]
        case 4:
            die_face = die_faces[3]
        case 5:
            die_face = die_faces[4]
        case 6:
            die_face = die_faces[5]                        
    
    return die_result, die_face

def header():
    clear_terminal()
    '''
    print the header of the program
    '''
    print(r'''
__     __                                  ____             
\ \   / / __ ___   __ _ ______ _          |  _ \  _____   __
 \ \ / / '_ ` _ \ / _` |_  / _` |  _____  | | | |/ _ \ \ / /
  \ V /| | | | | | (_| |/ / (_| | |_____| | |_| |  __/\ V / 
   \_/ |_| |_| |_|\__,_/___\__,_|         |____/ \___| \_/   
''')
    print('-' * 20, 'WELCOME TO ROLLING DICE 0.0 🎲', '-' * 20)
# main program

header()
user_input = input('\nPress enter to roll the die or q to quit: ')
roll = 0
while user_input.lower() != 'q':
    roll += 1
    header()
    
    result, face = roll_die()
    print(f'You roll a {result}!')
    print(face)
    print(f'Roll number: {roll}')
    print('-' * 25)
    user_input = input('\nPress enter to roll the die or q to quit: ')

print('Good bye!👋\n')
print('-' * 20, 'END OF THE PROGRAM', '-' * 20)
