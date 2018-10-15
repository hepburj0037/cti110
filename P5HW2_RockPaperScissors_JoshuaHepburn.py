# Create a rock, paper, scissor game.
# 10/1/2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Joshua Hepburn
#

# Import random module to use.
import random

# Function that creates a random number.
def randomnumbergeneraor():

    # Have a range for the choices to be chosen from.
    randomnumber = random.randint(1, 3)

    # Send it back inbto the function
    return randomnumber

# Have the computer make a random decision
def computersdecision(randomnumber):

    # Assign a a word to each computer decision.
    if randomnumber == 1:
        computrdecision = "rock"
    elif randomnumber == 2:
        computerdecision = "paper"
    elif randomnumber == 3:
        computerdecision = "scissors"

        # Send the computer choice back
        return computerdecision

# Get users answer from user before diplay of computers answer.
def userdecision():
    userschoice = input("Please enter your choice: ")

    # Send back users choice.
    return userschoice

# Display a funciton to choose the winner.
def choosewinner(computerdecision, userschoice):

    # Have a message after each match.
    rockrepot = "The rock smashes the scissors"
    paperreport = "Paper wraps rock"
    scissorreport = "Scissors cuts paper"
    winner = "No one won"
    report = ""
    
    if computerdecision == "rock" and userschoice == "scissors":
        winner = "Computer"
        report = rockreport
    elif computerdecision == "scissors" and userschoice == "rock":
        winner = "User"
        report = rockreport
        
    if computerdecision == "paper" and userschoice == "rock":
        winner = "Computer"
        report = paperreport
    elif computerdecision == "rock" and userschoice == "paper":
        winner = "User"
        report = paperreport
        
    if computerdecision == "scissors" and userschoice == "paper":
        winner = "Computer"
        report = scissorreport
    elif computerdecision == "paper" and userschoice == "scissors":
        winner = "User"
        report = scissorreport

    # Send answer back to user.
    return winner, report

# Create the main function to be put together.
def main():
    randomnumber = randomnumbergeneraor()
    computerschoise = computersdecision(randomnumber)
    userschoice = userdecision
    print("The computer chose", computerschoice)
    winner, report = choosewinner(computerschoise, userschoice)
    












