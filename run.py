# Terminal of 80 characters wide and 24 rows high

"""
Code bases on Love Sandwiches - to imports lists of words from google sheets
"""
import gspread
from google.oauth2.service_account import Credentials
import random # For selecting a random word

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-words')

easy_words = SHEET.worksheet('easy_words')

data = easy_words.row_values(1)

random_word = random.choice(data)

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


num_lives = 7

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

    # Check if letter guessed is a letter in the word
    for position in range(len(random_word)):
        letter_position = random_word[position]
        if letter_position == letter_guess:
            empty_guess[position] = letter_position

    if letter_guess not in random_word:
        num_lives -= 1
        if num_lives == 0:
            game_over = True
            print(f"Sorry, you've lost the answer was {random_word}")
    
    print(empty_guess)
    # Check if any _ are left 
    if "_" not in empty_guess:
        game_over = True
        print("Congratulations!!! You Win!!!")

    print(hangman_lives[num_lives])