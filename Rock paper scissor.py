import random

n = ["ROCK", "PAPER", "SCISSOR"]
w_user = 0
w_comp = 0
choice = 1
while choice != 2:

    # Random Computer choice
    comp = random.choice(n)

    #User Choice
    user = input("Enter rock,paper or scissor:")
    user_1 = user.upper()
    print("User-->", user_1)
    print("Computer->", comp)

    #Winning Cases
    if comp == "SCISSOR" and user_1 == "ROCK":
        print("\nUser Wins")
        w_user = w_user + 1
    elif user_1 == "SCISSOR" and comp == "ROCK":
        print("\nComputer Wins")
        w_comp = w_comp + 1
    elif comp == "PAPER" and user_1 == "ROCK":
        print("\nComputer Wins")
        w_comp = w_comp + 1
    elif user_1 == "PAPER" and comp == "ROCK":
        print("\nUser Wins")
        w_user = w_user + 1
    elif comp == "PAPER" and user_1 == "SCISSOR":
        print("\nUser Wins")
        w_user = w_user + 1
    elif comp == "SCISSOR" and user_1 == "PAPER":
        print("\nComp Wins")
        w_comp = w_comp + 1
    elif comp == user_1:
        print("\nTie")

    # Valid CHoice
    elif user_1 != "ROCK" or user_1 != "PAPER" or user_1 != "SCISSOR":
        print("Enter Valid Choice..")

    #Point Table
    print("Computer points--->", w_comp)
    print("User points--->", w_user)
    choice = int(input("Do you want to continue if yes press 1 or press 2:"))
