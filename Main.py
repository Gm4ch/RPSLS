#program to play rock paper scissors lizard spock with the user
from asyncore import loop
import random as r
import time as t
option_1 = "rock"
option_2 = "paper"
option_3 = "scissors"
option_4 = "lizard"
option_5 = "spock"

masterLoop = True
loop2 = True
loop3 = True

def logic():
#loosing logic 
    if pc_choice == option_1 and user_choice == option_4:
        print("you lose")
    elif pc_choice == option_1 and user_choice == option_3:
        print("you lose")
    elif pc_choice == option_2 and user_choice == option_1:
        print("you lose")
    elif pc_choice == option_2 and user_choice == option_5:
        print("you lose")
    elif pc_choice == option_3 and user_choice == option_4:
        print("you lose")
    elif pc_choice == option_3 and user_choice == option_2:
        print("you lose")
    elif pc_choice == option_4 and user_choice == option_2:
        print("you lose")
    elif pc_choice == option_4 and user_choice == option_5:
        print("you lose")
    elif pc_choice == option_5 and user_choice == option_1:
        print("you lose")
    elif pc_choice == option_5 and user_choice == option_3:
        print("you lose")
    #winning logic
    if user_choice == option_1 and pc_choice == option_4:
        print("you win")
    elif user_choice == option_1 and pc_choice == option_3:
        print("you win")
    elif user_choice == option_2 and pc_choice == option_1:
        print("you win")
    elif user_choice == option_2 and pc_choice == option_5:
        print("you win")
    elif user_choice == option_3 and pc_choice == option_4:
        print("you win")
    elif user_choice == option_3 and pc_choice == option_2:
        print("you win")
    elif user_choice == option_4 and pc_choice == option_2:
        print("you win")
    elif user_choice == option_4 and pc_choice == option_5:
        print("you win")
    elif user_choice == option_5 and pc_choice == option_1:
        print("you win")
    elif user_choice == option_5 and pc_choice == option_3:
        print("you win")
    #tie logic
    elif pc_choice == user_choice:
        print("its a tie")

#welcome
print("Welcome to Rock Paper Scissors Lizard Spock or \"RPSLS\"!",end=" ")

#rules
rules = input("would you like to read the rules? ")
while loop2 == True: #starting a loop for getting the right input
    if rules == "y" or rules == "yes": #if user wants rules print out the rules.
        print("Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, \nscissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")
        t.sleep(4)
        print("Got that? Cool. lets begin")
        t.sleep(1)
        loop2 = False #ending loop

    elif rules == "n" or rules == "no":
        print("ok! lets start the game.")
        loop2 = False
    else:
        print("this is not a valid input. ",end="")
        rules = input("would you like to read the rules?\t")

while masterLoop == True: #masterloop for the program

    user_choice = input("rock = 1\npaper = 2\nscissors = 3\nlizard = 4\nspock = 5\nplease enter the number of the move you make\t") # asking user what action they do
    while loop3 == True:
        if user_choice.isnumeric() == True: 
            user_choice = int(user_choice) #if the input is a number the program checks to see if its between the range of 1 and 5.
            if user_choice in range(1,6):
                loop3 = False
            else:
                user_choice = input("this is not an accepatable answer please enter a number between 1 and 5:  ")
        elif user_choice.isnumeric() == False:
            print("this is not an acceptable answer ",end="")
            user_choice = input("please enter a number between 1 and 5:  ")
        
#after the computer verifys that the user is entering an input that it can handle it turns it into an intiger
    user_choice = int(user_choice)
    pc_choice = r.randint(1,5)

#logic to make the users choice equal to the variables that are in use for my logic function
    if user_choice == 1:
        user_choice = option_1
    elif user_choice == 2:
        user_choice = option_2
    elif user_choice == 3:
        user_choice = option_3
    elif user_choice == 4:
        user_choice = option_4
    elif user_choice == 5:
        user_choice = option_5

    pc_choice = r.randint(1,5)
#logic to make the computers choice equal to the variables that are in use for my logic function
    if pc_choice == 1:
        pc_choice = option_1
    elif pc_choice == 2:
        pc_choice = option_2
    elif pc_choice == 3:
        pc_choice = option_3
    elif pc_choice == 4:
        pc_choice = option_4
    elif pc_choice == 5:
        pc_choice = option_5
#telling the user who chose what
    print("the computer chose: ",pc_choice)
    print("you chose:",user_choice)
    logic()
#asking user if they would like to play agian
    play_again = input("do you want to play again? ")
    if play_again == "yes" or play_again == "y":
        print("")
        #if the user does want to play again we reset all the loops and variables.
        user_choice = None
        pc_choice = None
        masterLoop = True
        loop2 = True
        loop3 = True
    else:
        print("bye! see you next time. (gm)")
        masterLoop = False
