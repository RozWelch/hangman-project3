"""
Code for google sheets basesd on Love Sandwiches tutorial - to imports lists of words 
"""
import gspread # for accessing google sheet for word list
from google.oauth2.service_account import Credentials 
import random # For selecting a random word
import os # For clearing the Terminal

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman-words')

"""
Colorama - for using coloured text on the terminal
"""
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

"""
Function for clearing the terminal screen
"""
def clear_console():
    os.system('clear')

"""
For showing HangCow lives stage
"""
hangman_lives = [Fore.RED + '''
    *--------------*
    |              |
    |           __n__n__
    |    .------`-\**/-'
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
    |   /         (oo)
    |  / \.  __   ./
    |     |//YY \|/
    |     |||   |||
    ===============
''', '''
    *--------------*
    |              |
    |           __n__n__
    |    .------`-\OO/-'
    |   /         (oo)
    |  / \.  __   ./
    |     |//   \|/
    |     |||   |||
    ===============
''', '''
    *--------------*
    |              |
    |           __n__n__
    |    .------`-\OO/-'
    |   /         (oo)
    |  / \.  __   ./
    |     |//   \|
    |     |||   ||
    ===============
''', '''
    *--------------*
    |              |
    |           __n__n__
    |    .------`-\OO/-'
    |   /         (oo)
    |  / \.  __   ./
    |     |//   
    |     |||   
    ===============
''', '''
    *--------------*
    |              |
    |           __n__n__
    |    .------`-\OO/-'
    |   /         (oo)
    |  / \.  __   ./
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

win_message = (Fore.GREEN + """
  __        ___                        _              __n__n__
  \ \  /\  / / _ _ __  _ __   ___ _ __| |      .------`-\^^/-'
   \ \/  \/ / | | '_ \| '_ \ / _ \ '__| |     /  ##  ## (oo)  <Moo!>
    \  /\  /  | | | | | | | |  __/ |  |_|    / \## __   ./
     \/  \/   |_|_| |_|_| |_|\___|_|  (_)       |//YY \|/
                                                |||   |||    
   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||  \n
""")

"""
Function for main page display
"""
def main_screen():
  clear_console()
  print(Fore.GREEN + """
   _    _                    _____                         __n__n__
  | |  | |                  / ____|                 .------`-\OO/-'
  | |__| | __ _ _ __   __ _| |     _____      __   /  ##  ## (oo)
  |  __  |/ _` | '_ \ / _` | |    / _ \ \ /\ / /  / \## __   ./
  | |  | | (_| | | | | (_| | |___| (_) \ V  V /      |//YY \|/
  |_|  |_|\__,_|_| |_|\__, |\_____\___/ \_/\_/  |||  |||   |||
                       __/ ||||||||||||||||||||||||||||||||||||||||
                      |___/                     
  """)
  print(Fore.CYAN + '  Welcome to HangCow.\n  The rules are just like Hangman but with a cow theme!\n')
  print('  You have 9 lives to guess the word - \n  for each incorrect guess you loose a life.\n')
  select_level()

"""
Function to select a difficulty level
"""
def select_level():
  while True:
    try:
      selection = input('  Select a difficulty level:\n  1 for Easy, 2 for Medium, or 3 for Difficult:\n  ')
      if selection == '1':
        easy_words = SHEET.worksheet('easy_words')
        data = easy_words.row_values(1)
        random_word = random.choice(data)
        play_game(random_word)
      if selection == '2':
        medium_words = SHEET.worksheet('medium_words')
        data = medium_words.row_values(1)
        random_word = random.choice(data)
        play_game(random_word)
      if selection == '3':
        difficult_words = SHEET.worksheet('difficult_words')
        data = difficult_words.row_values(1)
        random_word = random.choice(data)
        play_game(random_word)
    except ValueError:
      print('Please enter 1, 2, or 3')
      
"""
Function to play the game
"""
def play_game(random_word):

    clear_console()
    print(Fore.CYAN + '  Best of luck!')
    # Add a _ for each letter in the random word
    empty_guess = []
    for space in random_word:
      empty_guess += "_"

    game_over = False
    lives_remaining = 9

    while game_over == False:
      # Get guess from user
      
      print(hangman_lives[lives_remaining])
      print(f"  {' '.join(empty_guess)}\n")
      letter_guess = input("  Guess a letter:\n  ").lower()
      clear_console()

      # Check if entry is a valid input
      if len(letter_guess) == 1 and letter_guess.isalpha():
        # Check if entry has aready been made
        if letter_guess in empty_guess:
          print(Fore.RED + f"  You've already guessed '{letter_guess}', try again")
        # Check if letter guessed is a letter in the word
        for position in range(len(random_word)):
          letter_position = random_word[position]
          if letter_position == letter_guess:
            empty_guess[position] = letter_position
            print(Fore.YELLOW + f"  Yes, '{letter_guess}' is in the word.")
        # If letter not in word, loose a life, if no lives left print loose message
        if letter_guess not in random_word:
          lives_remaining -= 1
          print(Fore.RED + f'  Not a correct guess, you loose a life. You have {lives_remaining} lives left')
        if lives_remaining == 0:
          game_over = True
          clear_console()
          print(Fore.RED + f"  Sorry, you've lost the answer was {random_word}")
          print(hangman_lives[lives_remaining])
          play_again()
    
        # Check if any _ are left, if not print win message
        if "_" not in empty_guess:
          game_over = True
          clear_console()
          print(Fore.YELLOW + "  Congratulations!!! You Win! Your cow is free!\n")
          print(win_message)
          play_again()
    
      else:
        print(Fore.RED + '  Not a valid entry, please try again')
           
def play_again():
  play_again_answer = input('  Press Y to play again:\n  ').lower()
  if play_again_answer == 'y':
    main()


"""
Main function to play the game
"""
def main():
  main_screen()
  
main()