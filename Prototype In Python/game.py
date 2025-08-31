#Eesa Aslam
#Arkwright Project

import random 
import sys
import time
def menu():
    """Here the user is  shown a menu and has to pick something"""
    print()
    print("Start Game")
    print("Leaderboard")
    print("Quit")
    print()

    user_choice = input("Enter what you want to do : ").lower()

    if user_choice in ["Start game","start"]:
        game() #Here it runs the game function when the user enters Start Game

    if user_choice in ["leaderboard","scores","lb"]:
        show_leaderboard() #Here the Leaderboard function is run

    if user_choice in ["quit","exit","q"]:
        Exit() #Here the Exit function is run 


def game():
    #Asking Players for their name 
    P1 = input("\nPlease enter your name : ")
    P2 = input("\nPlease enter your name : ")
    #If P1 has same name as P2 then it would say to re enter your name again
    while P1 == P2:
        print("Sorry you cant have the same name please try again")
        P1 = input("\nPlease enter your name : ")
        P2 = input("\nPlease enter your name : ")

    score_P1 = 0
    score_P2 = 0

    #Repeats the rolling_dice function for 5 rounds 
    for round_number in range(1,6):
        print(f"\n--- Round {round_number} ---")
    
        P1_dice1, P1_dice2 = roll_two_dice(P1)
        score_P1 = update_score(P1,P1_dice1, P1_dice2)

        P2_dice1, P2_dice2 = roll_two_dice(P2)
        score_P2 = update_score(P2,P2_dice1, P2_dice2)

        
    #Compares the scores of both players and prints a msg saying who won 
    if score_P1 < score_P2:
        print()
        print(P1,"wins!")
        print()
    else:
        print()
        print(P2,"wins!")
        print()

    #If scores are equal theres a tie breaker and the tie_breaker function is run 
    if score_P1 == score_P2:
        print("f\n Ok each player now gets an extra roll")
        tie_breaker(P1, P2, score_P1, score_P2)

    #These store the player with the most score under 2 variables winner_name and winner_score whcih are used for the leaderboard
    if score_P1 > score_P2:
        winner_name = P1
        winner_score = score_P1
    elif score_P2 > score_P1:
        winner_name = P2
        winner_score = score_P2

    leaderboard(winner_name,winner_score)
    
    
    time.sleep(1)
    menu()
#Exits the program
def Exit():
    print()
    print("Exiting the game......")
    print()
    exit()


def roll_two_dice(player_name):
    print(f"\n{player_name}, click enter to roll") #Says to the player to roll their dice
    input()
    print("rolling...")
    time.sleep(1) # makes sure theres a 1 second pause after rolling
    dice_roll1 = random.randint(1,6) #random number is picked for both dice from a range of 1-6
    dice_roll2 = random.randint(1,6) #random number is picked for both dice from a range of 1-6
    print("You rolled: ", dice_roll1, "and", dice_roll2)
    return dice_roll1, dice_roll2 #returns the value rolled 

#This is how score is worked out 
def update_score(player_name,dice_roll1,dice_roll2):
    dice_sum = dice_roll1 + dice_roll2 #Two dice results are added 
    
    if dice_sum % 2 == 0:  # if the result is even the sum increases by 10 
        dice_sum += 10
        print(f"\n{player_name}, your sum is even! +10 points") 
    else:
        dice_sum -= 5 #if its odd the sum is decreased by 5
        print(f"\n{player_name}, your sum is odd! -5 points")
    if dice_sum < 0:
        dice_sum = 0

    print(f"New score: {dice_sum}") # New score is displayed 
    return dice_sum

def tie_breaker(P1,P2,score_P1,score_P2):
    while score_P1 == score_P2: 
        P1_dice1, P1_dice2 = roll_two_dice(P1)
        score_P1 += update_score(P1,P1_dice1, P1_dice2) #The roll_two_dice function and update_score is repeated for both players for their final roll  

        P2_dice1, P2_dice2 = roll_two_dice(P2)
        score_P2 += update_score(P2,P2_dice1, P2_dice2)

    if score_P1 < score_P2:
        print(P1,"has won the tie breaker and wins!")
    else:                                           #whoever has the most score overall wins 
        print(P2,"has won the tie breaker and wins!")

    time.sleep(1)    
    menu()
    return score_P1,score_P2 #The score isthen updated

def leaderboard(winner_name, winner_score):
    with open("scores.txt", "w") as file:
        file.write("") #The file is opened 
    with open("scores.txt", "a") as file:
        file.write(f"{winner_name} - {winner_score}\n") #This writes inside the file where info is stored the winners name and score

#This is how you see the leaderboard in the menu
def show_leaderboard():
    try:
        with open("scores.txt", "r") as file:
            scores = file.readlines() # This reads the file and displays the text 

        print("\n--- Game History ---")
        for entry in scores:
            print(entry.strip())  # strip removes the extra newline
    except FileNotFoundError: #If the user trys to check the leaderboard they are shown this msg.
        print("No scores yet! Play a game first.") 

    time.sleep(1)
    menu()

menu()

