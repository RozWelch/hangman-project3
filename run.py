# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# List of words to select randomly from
list_of_words = ["imagination", "tea", "client", "cookie", "mode", "setting", "injury", "university", "night", "appearance", "refrigerator", "freedom", "definition", "category", "desk", "awareness", "perception", "buyer", "user""]
import random
random_word = random.choice(list_of_words)

# Get guess from user
letter_guess = input("Guess a letter: ").lower()

# Check if letter guessed is a letter in the word
for letter in random_word:
    if letter == guess:
        print("Correct")
    else:
        print("Incorrect")