# For this project, you will individually create a program that has a "player" and a "computer" advisary.
#  The computer should randomly choose it's decision based on a list of actions it can take 
# ("Rock", "Paper" or "Scissors"). The player should then have a chance to input their decision.
#  If player and computer choose the same decision then display ("Game Tied"),
#  If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"), 
# if the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose"), 
# and if the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose")
#  -- Vice versa for other descisions.

# Continue to ask the player for their input until they say "I quit", 
# at which time the game will then end and display ("Thank you for playing").

# In this project, you will need to use the random.randint function to enable to computer to make a random decision.
#  Full documentation on the use of this function is attached in a link to this assignment.

# Once completed, commit your code to github and submit the link to this assignment.

import time
import random

class RPC(): 
    """ 
    Attributes for the class: 
    -player_choices expected to be an empty list 
    -comp_choices expected to be an empty list
    """


    def __init__(self, player_choices, comp_choices): 
        self.player_choices = player_choices
        self.comp_choices = comp_choices
    
    def startGame(self): 
        print("Starting Game...")
        print('...')
        time.sleep(1)
        
        while True: 
            player_selection = input("Your turn! Choose, rock, paper or scissors.")
            print('...')
            if player_selection.lower() == "i quit": 
                print("Thank you for playing")
                quit()
            elif player_selection.lower() == 'rock' or player_selection.lower() == 'scissors' or player_selection.lower() == 'paper':
                self.player_choices.append(player_selection)
                break
            else: 
                print("Please enter a valid input.")
                continue 
    
    def computerTurn(self): 
        options = ['rock', 'paper', 'scissors']
        print("The computer chooses:")
        random.shuffle(options) 
        self.comp_choices.append(options[0])
        for choice in self.comp_choices: 
            print(choice)
            print('...')
    
    def evaluate(self): 
        while True:
            if self.comp_choices == self.player_choices: 
                print("It's a tie!")
                self.comp_choices.clear()
                self.player_choices.clear()
                break
            elif (self.comp_choices[0] == 'rock' and self.player_choices[0] == 'scissors'):
                print("The computer wins!")
                self.comp_choices.clear()
                self.player_choices.clear() 
                break
            elif (self.comp_choices[0] == 'rock' and self.player_choices[0] == 'paper'):
                print("You win!")
                self.comp_choices.clear()
                self.player_choices.clear() 
                break
            elif (self.comp_choices[0] == 'paper' and self.player_choices[0] == 'scissors'):
                print("You win!")
                self.comp_choices.clear()
                self.player_choices.clear()
                break
            elif (self.comp_choices[0] == 'paper' and self.player_choices[0] == 'rock'): 
                print("The computer wins!")
                self.comp_choices.clear()
                self.player_choices.clear()
                break
            elif (self.comp_choices[0] == 'scissors' and self.player_choices[0] == 'paper'):
                print("The computer wins!")
                self.comp_choices.clear()
                self.player_choices.clear()
                break
            elif (self.comp_choices[0] == 'scissors' and self.player_choices[0] == 'rock'):
                print("You win!")
                self.comp_choices.clear()
                self.player_choices.clear()
                break
            else: 
                print("Please enter a valid input.")
                break

       
my_RPC = RPC([], [])

def playGame(): 
    while True:
        my_RPC.startGame()
        my_RPC.computerTurn()
        my_RPC.evaluate()
        question = input("Play again?")
        if question.lower() == 'yes': 
            continue
        elif question.lower() == 'no': 
            print("Thank you for playing.")
            quit()
        else: 
            print("Please enter a valid input.")


playGame()