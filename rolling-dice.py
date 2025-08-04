# AUThOR: Victor Maza
# DATE: 22/6/25
"""
simple program to simulate rolling a dice with dinamic faces
"""

# modules
import random

# functions

def clear_terminal():
    """
    clear the terminal screen
    """
    print("\033c", end="")

def roll_die():
    """
    Generate a random die roll and return the result and its visual representation.

    Returns
    -------
    int
        The die result (1 to 6).
    list of list of str
        A 3x3 matrix representing the die face with "x" marks.  
    """

    dice_face = [["", "", ""],
                 ["", "", ""],
                 ["", "", ""]]

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
        dice_face[row][colummn] = "x"

    return die_result, dice_face


def header():
    """
    print the header of the program
    """
    clear_terminal()
    print(r"""
__     __                                  ____             
\ \   / / __ ___   __ _ ______ _          |  _ \  _____   __
 \ \ / / '_ ` _ \ / _` |_  / _` |  _____  | | | |/ _ \ \ / /
  \ V /| | | | | | (_| |/ / (_| | |_____| | |_| |  __/\ V / 
   \_/ |_| |_| |_|\__,_/___\__,_|         |____/ \___| \_/   
""")
    print("-" * 20, "WELCOME TO ROLLING DICE 1.2 🎲", "-" * 20)

def main_menu():
    header()
    print("")
    print("-" * 20, "Main menu", "-" * 20)
    print("""
    1- Roll a dice
    2- Generala game
    3- Rolling to obtain generala
    4- Exit          
""")
    while True:
        try:
            user_input = int(input("Choose an option: "))
            return user_input
        except ValueError:
            print("Invalid option\n")
    # me quede aca, me falta hacer las diferentes opciones, asi como esta solo tira 6 dados

# main program

main_menu()
user_input = input("\nPress enter to roll the die or q to quit: ")
roll = 0
while user_input.lower() != "q":
    roll += 1
    header()
    results = []
    dice_face = []

    for i in range(6):
        result, face = roll_die()
        results.append(result)
        dice_face.append(face)

    print(f'You roll a {", ".join(str(num) for num in results)}!')

    print(f'''
    +-------+    +-------+   +-------+                                                  
    | {dice_face[0][0][0]:<2}{dice_face[0][0][1]:<2}{dice_face[0][0][2]:<2}|    | {dice_face[1][0][0]:<2}{dice_face[1][0][1]:<2}{dice_face[1][0][2]:<2}|   | {dice_face[2][0][0]:<2}{dice_face[2][0][1]:<2}{dice_face[2][0][2]:<2}|
    | {dice_face[0][1][0]:<2}{dice_face[0][1][1]:<2}{dice_face[0][1][2]:<2}|    | {dice_face[1][1][0]:<2}{dice_face[1][1][1]:<2}{dice_face[1][1][2]:<2}|   | {dice_face[2][1][0]:<2}{dice_face[2][1][1]:<2}{dice_face[2][1][2]:<2}|
    | {dice_face[0][2][0]:<2}{dice_face[0][2][1]:<2}{dice_face[0][2][2]:<2}|    | {dice_face[1][2][0]:<2}{dice_face[1][2][1]:<2}{dice_face[1][2][2]:<2}|   | {dice_face[2][2][0]:<2}{dice_face[2][2][1]:<2}{dice_face[2][2][2]:<2}|
    +-------+    +-------+   +-------+
''', end = " ")
    print(f'''
    +-------+    +-------+   +-------+                                                  
    | {dice_face[3][0][0]:<2}{dice_face[3][0][1]:<2}{dice_face[3][0][2]:<2}|    | {dice_face[4][0][0]:<2}{dice_face[4][0][1]:<2}{dice_face[4][0][2]:<2}|   | {dice_face[5][0][0]:<2}{dice_face[5][0][1]:<2}{dice_face[5][0][2]:<2}|
    | {dice_face[3][1][0]:<2}{dice_face[3][1][1]:<2}{dice_face[3][1][2]:<2}|    | {dice_face[4][1][0]:<2}{dice_face[4][1][1]:<2}{dice_face[4][1][2]:<2}|   | {dice_face[5][1][0]:<2}{dice_face[5][1][1]:<2}{dice_face[5][1][2]:<2}|
    | {dice_face[3][2][0]:<2}{dice_face[3][2][1]:<2}{dice_face[3][2][2]:<2}|    | {dice_face[4][2][0]:<2}{dice_face[4][2][1]:<2}{dice_face[4][2][2]:<2}|   | {dice_face[5][2][0]:<2}{dice_face[5][2][1]:<2}{dice_face[5][2][2]:<2}|
    +-------+    +-------+   +-------+
''')
    
    print(f'Roll number: {roll}')
    print('-' * 25)
    user_input = input('\nPress enter to roll the die or q to quit: ')


print('Good bye!👋\n')
print('-' * 20, 'END OF THE PROGRAM', '-' * 20)