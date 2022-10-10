## HANGCOW 
Hangcow is a fun game based on Hangman, but with a cow theme! It is a terminal based game, run on the Code Institute terminal on Heroku. Users try to guess a random word, until they are successful in guessing the work, or they run out of lives.

Link to the site here https://hangcow.herokuapp.com/

## Am I Responsive mockups
![Responsive Mockup](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/amiresponsive.jpg)

## Contents
* [How to play](#How-to-play)
* [Design](#Design)
* [Features and User experience](#Features-and-User-experience)
* [Technologies Used](#Technologies-Used)
* [Fixed and Unfixed Bugs](#Fixed-and-Unfixed-Bugs)
* [Validation](#Validation)
* [Testing](#Testing)
* [Project Creation and Deployment](#Project-Creation-and-Deployment)
* [Credits](#Credits)

## How to play

Hangcow follows the same rules as Hangman. A user will select a level easy, medium or difficult. A random word is selected, and '_' shown for each letter in the word. A user guesses a letter. The input is checked to see if it is an alphabetic, single letter. If not they are asked to input a letter again. If the letter is in the word, the correct letter is shown in its position in the word. If the letter is not in the word they loose a life. The user continues to guess until they run out of lives without guessing the word, when a 'You loose' message is displayed; or they correctly guess the word, then a 'You win' message is displayed.

## Design 

The game was designed to be easy to play, and also fun.
I looked online at hangman games, and worked out the logic of how the game should work. 
Initially a flow chart was created to work out where the user should input data, how to validate that data, and what happens for a correct or incorrect entry. I worked out how the game should end: 
![Flowchart](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/flowchart.gif)

## Features and User experience

* Main Screen:
    * The main screen displays the rules and allows the user to select a difficulty level
    * An animated logo adds interest to the game
    * UX: as a first time user I want to easily find out how to play the game 

![Mainscreen](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/mainscreen.jpg)
    
* The user is asked to select a difficulty level
    * UX: as a first time or returning user, I want to easily select a difficulty level

![Difficulty](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/setdifficulty.jpg)

* Main Game Play Screen:
    * a graphic is displayed to show the user the lives remaining
    * underneath a '_' is shown for each letter in the word
    * UX: as a first time or returning user, I want to see what stage I am at in the game
    * UX: as a first time or returning user, I want to see how many letters in the word I have to guess

![firststage](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/firststage.jpg)

* Correct, incorrect guesses or have already guessed messages:
    * the user is given feedback on their input
    * UX: as a first time or returning user, I want to receive feedback on my guesses

![lettercorrect](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/lettercorrect.jpg)
![incorrectletter](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/incorrectletter.jpg)
![letteralreadyentered](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/letteralreadyentered.jpg)

* Winner screen and animation:
    * plays a winner animation if the user wins
    * UX: as a first time or returning user, I want a fun way to find out I have won

![winnerscreen](https://github.com/RozWelch/hangman-project3/blob/main/assets/readmeimages/winnerscreen.jpg)

* Future Features: 
    * A feature to take a user's name and if they've played before display their previous score
    * A table at the end of the game to show the top 5 scores

## Technologies Used

* Languages: Python 
* Libraries:  
    * Random: To select a random word
    * Os:for clearing the terminal
    * Colorama: To add colour text to the terminal
    * Time: For timing the animations
* API: gspread: To read the google sheet  

## Fixed and Unfixed Bugs

* Fixed bugs:
    * When I wrote the code for the game I didn't have it defined within a function. I then moved it into the main game function. This caused my if statements to be incorrectly tabbed, and the game was not taking off a life correctly. I fixed it by retabbing the function and tested it and it worked properly again. 
    * When I made the main game function, the game over function was not working properly, I changed an 'elif' to an 'if' and this solved the problem.

* No known unfixed bugs

## Validation 

* When tested the website generally recommended pep8online.com was down. 
    * As a workaround, a PEP8 validator was used in the Gitpod Workspace directly by following these steps:
    * Run the command pip3 install pycodestyle (Note that this extension may already be installed, in which case this command will do nothing.)
    * In my workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
    * Type the word linter into the search bar that appears, and click on Python: Select Linter from the filtered results.
    * Select pycodestyle from the list.
    * PEP8 errors would be underlined in red, as well as being listed in the PROBLEMS tab beside your terminal.

* Fixed: Extra spaces in code. Comments incorrectly added. Removed extra trailing spaces as hilighted.   
* The ascii art was causing 'invalid escape sequence' warnings. I checked with tutor support and this was ok as they are just ascii artwork.  

## Testing

* Tested on the local terminal, and tested the deployed site on Google Chrome on a mac and also a laptop

* Main Screen:
    * Tested: Animation displays properly on local and deployed versions
    * Tested: Selection of 1, 2 or 3 selects correct list of words from google sheet
    * Tested: Input of entry other than 1, 2 or 3 asks the user to submit again

* Main Game:
    * Tested: Entering a correct letter adds the letter to space on word
    * Tested: Entering an incorrect letter takes away a life and adds to the HangCow lives graphic
    * Tested: Entering a letter already guessed lets the user know, and allows the user guess again
    * Tested: Entering a invalid entry displays a message and allows the user to guess again
    * Tested: Finishing the word correctly brings the user to the winner screen
    * Tested: Loosing all your lives brings the user to the loosing screen
    * Tested: Pressing any key at the end of the game brings the user back to the main screen

## Project Creation and Deployment

The project was created in Git Hub using the Code Institute template.

The following commands were used throughout the project:
* git add . - This command was used to add files to the staging area before committing.
* git commit -m "I add commit message here" - This command was used to to commit changes to the local repository.
* git push - This command is used to push all committed changes to the GitHub repository. 

* Deployment    
    * From the Heroku dashboard I clicked the create new app button, named the app and selected the Europe region and clicked 'Create app'
    * Then I clicked on the settings tab and set up the Config Vars: Key was CREDS, I copied the CREDS.json file into the value field, then clicked 'Add'. I also set up a Config Var - Key was PORT and value was 8000
    * Next I clicked 'Add Build pack' and added: Python first and then node.js, clicking 'Save' after each.
    * Then I went to the deploy section and selected connect to GitHub and selected my project name, and clicked connect to link up. I enabled automatic deploys for this project.
    * The app is then built, and we get an app was successfully built message and a button to take me to the deployed link.
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

How to add Python sleep - for timing the animations:
https://realpython.com/python-sleep/

Acknowledgements: Thanks to my mentor, my facilitator, my fellow students on Slack, tutoring support and to my friends for helping test the site.