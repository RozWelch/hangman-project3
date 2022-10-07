## HANGCOW 
Hangcow is a fun game based on Hangman, but with a cow theme! It is a terminal based game, run on the Code Institue terminal on Heroku. Users try to guess a random word, until they are sucessful in guessing the work, or they run out of lives.

Link to the site here https://hangcow.herokuapp.com/

## Am I Responsive mockups
(add link)

## Contents
* How to play
* Design Stage
* Features and User experience
* Technologies Used
* Fixed and Unfixed Bugs
* Validating and Testing
* Deployment
* Credits


## How to play

Hangcow follows the same rules as Hangman. A user will select a level easy, medium or difficult. A random word is selected, and '_' shown for each letter in the word. A user guesses a letter. The input is checked to see if it is an alphabetic, single letter. If not they are asked to input a letter again. If the letter is in the word, the correct letter is shown in its position in the word. If the letter is not in the word they loose a life. The user continues to guess until they run out of lives without completing the work, when a 'You loose' message is displayed; or they correctly guess the word, when a 'You win" message is displayed.

## Design Stage

The game was designed to be easy to play, and also fun.
Initially a flow chart was created: 


## Features and User experience

Add images and text

## Technologies Used

* Languages: Python 
* Libraries:  
    * Random: To select a random word
    * Os:for clearing the terminal
    * Colorama: To add colour text to the terminal

## Fixed and Unfixed Bugs

Add text

## Validation and Testing

* add text

## Deployment

* From the Heroku dashboard I clicked the create new app button, named the app and selected the Europe region and clicked 'Create app'
* Then I clicked on the settings tab and set up the Config Vars: Key was CREDS, I copied the CREDS.json file into the value field, then clicked 'Add'. I also set up a Config Var - Key was PORT and value was 8000
* Next I clicked 'Add Build pack' and added: Python first and then node.js, clicking 'Save' after each.
* Then I went to the diploy section and selected connect to GitHub and selected my project name, and clicked connect to link up. I enabled automatic diploys for this project.
* The app is then built, and we get an app was sucessfully built message and a button to take me to the deployed link.
* I then tested the game, to check it works as per the terminal version. 

## Credits
Code Institute for the mock terminal to deploy to a live site.

Hangman ascii art:
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
https://ascii.co.uk/art/hangman
Hangman Tutorial (just watched for understanding, but I used my own code)
https://www.youtube.com/watch?v=m4nEnsavl6w

How to add colours to terminal:
https://www.youtube.com/watch?v=u51Zjlnui4Y

How to clear the console:
https://appdividend.com/2022/06/03/how-to-clear-console-in-python/#:~:text=For%20the%20Windows%20system%2C%20to,('cls').

Ascii art
Cow: https://www.asciiart.eu/animals/cows
Text: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

Acknowledgements: Thanks to my mentor, my facilitator, my fellow students on Slack, tutoring support and to my friends for helping test the site.