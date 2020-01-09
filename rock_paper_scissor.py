#user input
#computer input(random input)
#play game
    #check win
    #check tie
#end game


import random
items = ["rock", "paper", "scissors"]


def user_choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("Select Your Option by Writng The Index or by The", end = ' ')
    print("Whole Spelling\n")
    u_choice = input("Enter Your Choice :")
    u_choice = u_choice.lower()
    valid = True
    while valid:
        if u_choice not in items or u_choice not in ["1", "2", "3"]:
            print("\nYou May Have Enter Something Out of Context or", end = ' ')
            print("May be The Spelling or Index is Wrong.")
            u_choice = input("Enter Your Choice :")
            u_choice = u_choice.lower()
        else:
            valid = False
    return u_choice

def computer_choice():
    print("\n")
    print("Now It's Computer's Turn........")
    com_choice = random.choice(items)
    return com_choice


def play_game():
    print("LET'S PLAY ROCK, PAPER, SCISSOR!\n")
    print("\n")
    u_choice = user_choice()
    com_choice = computer_choice()
    check_if_win(u_choice, com_choice)
    check_if_tie(u_choice, com_choice)

            
