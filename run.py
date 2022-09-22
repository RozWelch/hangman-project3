"""
Code bases on Love Sandwiches - to imports lists of words from google sheets
"""
import gspread # for accessing google sheet for word list
from google.oauth2.service_account import Credentials 
import random # For selecting a random word
import os # For clearing the Termainal

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-words')


# Functin for clearing the Termainal
def clear_console():
    os.system('clear')

hangman_lives = ['''
*--------------*
|              |
|           __n__n__
|    .------`-\OO/-'
|   /  ##  ## (oo)
|  / \## __   ./
|     |//YY \|/
|     |||   |||
===============
''', '''
*--------------*
|              |
|           __n__n__
|    .------`-\OO/-'
|   /  ##  ## (oo)
|  / \## __   ./
|     |//YY 
|     |||   
===============
''', '''
*--------------*
|              |
|           __n__n__
|    .------`-\OO/-'
|   /  ##  ## (oo)
|  / \## __   ./
|     
|       
===============
''', '''
*--------------*
|              |
|           __n__n__
|    .------`-\OO/-'
|   /         (oo)
|  /      
|     
|       
===============
''', '''
*--------------*
|              |
|           __n__n__
|    .------`-\OO/-'
|             (oo)
|         
|     
|       
===============
''', '''
*--------------*
|              |
|           __n__n__
|            -\OO/-'
|             (oo)
|         
|     
|       
===============
''', '''
*--------------*
|              |
|           
|            
|             
|         
|     
|       
===============
''']

num_lives = 6

# Select difficulty level
print('Welcome to Hangcow! The rules are just like Hangman but with a cow theme.')
selection = input('Select a difficulty level: 1 for Easy, 2 for Medium, or 3 for Difficult:')
if selection == '1':
    easy_words = SHEET.worksheet('easy_words')
    data = easy_words.row_values(1)
    random_word = random.choice(data)
elif selection == '2':
    medium_words = SHEET.worksheet('medium_words')
    data = medium_words.row_values(1)
    random_word = random.choice(data)
elif selection == '3':
    difficult_words = SHEET.worksheet('difficult_words')
    data = difficult_words.row_values(1)
    random_word = random.choice(data)
clear_console()

# Testing code
print(f"for testing the code the solution is {random_word}")

# Add a _ for each letter in the random word
empty_guess = []
for space in random_word:
    empty_guess += "_"
print(empty_guess)

game_over = False

# Take guesses from user until all _ are filled
while game_over == False:
  # Get guess from user
  letter_guess = input("Guess a letter: ").lower()
  # Check if entry is a valid input
  if len(letter_guess) == 1 and letter_guess.isalpha():
    # Check if letter guessed is a letter in the word
    for position in range(len(random_word)):
        letter_position = random_word[position]
        if letter_position == letter_guess:
            empty_guess[position] = letter_position

    # If letter not in word, loose a life, if no lives left print loose message
    if letter_guess not in random_word:
        num_lives -= 1
        if num_lives == 0:
            game_over = True
            print(f"Sorry, you've lost the answer was {random_word}")
    
    print(empty_guess)
    # Check if any _ are left, if not print win message
    if "_" not in empty_guess:
        game_over = True
        print("Congratulations!!! You Win!!!")

    print(hangman_lives[num_lives])
    
  else:
    print('Not a valid entry, please try again')