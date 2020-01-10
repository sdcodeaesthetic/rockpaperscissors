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
    print("\nSelect Your Option by Writng The Index or by The", end = ' ')
    print("Whole Spelling")
    u_choice = input("Enter Your Choice :")
    u_choice = u_choice.lower()
    valid = True
    while valid:
        if u_choice not in items and u_choice not in ["1", "2", "3"]:
            print("\nYou May Have Enter Something Out of Context or", end = ' ')
            print("May be The Spelling or Index is Wrong.")
            u_choice = input("Enter Your Choice :")
            u_choice = u_choice.lower()
        else:
            valid = False
    if u_choice in ["1", "2", "3"]:
        idx = int(u_choice) - 1
        u_choice = items[idx]
    return u_choice

def computer_choice():
    print("\n")
    print("Now It's Computer's Turn........")
    com_choice = random.choice(items)
    return com_choice


def play_game():
    print("LET'S PLAY ROCK, PAPER, SCISSORS!")
    print("\n")
    u_choice = user_choice()
    com_choice = computer_choice()
    if(u_choice == items[0] and com_choice == items[1]):
        print("Computer Wins.")
    elif(u_choice == items[0] and com_choice == items[2]):
        print("You Win.")
    elif(u_choice == items[1] and com_choice == items[2]):
        print("Computer Wins.")
    elif(u_choice == items[1] and com_choice == items[0]):
        print("You Win.")
    elif(u_choice == items[2] and com_choice == items[0]):
        print("Computer Wins.")
    elif(u_choice == items[2] and com_choice == items[1]):
        print("You Win.")
    else:
        print("The Game is Tie.")
    while True:
        print("\nDo You Want To Play More ?")
        print("Press 1 To Play More")
        print("Press 2 To Quit")
        flag = input("> ")
        flag = int(flag)
        if(flag == 1):
            play_game()
        elif(flag == 2):
            quit()
        else:
            print("Invalid Input")


play_game()    
