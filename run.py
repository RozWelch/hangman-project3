# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# List of words to select randomly from
list_of_words = ["imagination", "tea", "client", "cookie", "mode", "setting", "injury", "university", "night", "appearance", "refrigerator", "freedom", "definition", "category", "desk", "awareness", "perception", "buyer", "user"]
import random
random_word = random.choice(list_of_words)

# Testing code
print(f"for testing the code the solution is {random_word}")

# Add a _ for each letter in the random word
empty_guess = []
for space in random_word:
    empty_guess += "_"
print(empty_guess)

# Get guess from user
letter_guess = input("Guess a letter: ").lower()

# Check if letter guessed is a letter in the word
for letter in random_word:
    if letter == letter_guess:
        print("Correct")
    else:
        print("Incorrect")