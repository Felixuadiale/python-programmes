import random
def get_user_choice():
    user_choice=str(input("Enter your choice(rock paper or scissors)")).lower()
    while user_choice not in ["rock","paper","scissors"]:
        print("Invalid choice.please enter rock , paper, scissors.")
        user_choice=input("Enter your choice(rock,paper, scissors)").lower()
    return user_choice
def get_computer_choice():
        return random.choice( ["rock","paper","scissors"])
def play_game():
        print("Welcome to rock, paper,scisors")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"you chose{user_choice}.")
        print(f"computer chose{computer_choice}.")
        result= determine_winner(user_choice,computer_choice)
        print(result) 
def determine_winner(user_choice,computer_choice):
    if user_choice== computer_choice:
        return"its a tie"
    elif(user_choice=="rock" and computer_choice == "sciisors") or\
     (user_choice=='paper' and computer_choice=="rock")or \
     (user_choice=="scissors"and computer_choice== "paper"):
        return "you win"
    else:
        return"Computer wins"
if __name__=="__main__":
     play_game()