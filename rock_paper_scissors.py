import random

print('\nWelcome to our game of Rock Paper Scissors\n')
game_on = True

# COMPUTER'S CHOICE

def random_selection():
    game_option = ['R', 'P', 'S']
    computer_choice = random.choice(game_option)
    print('computer\'s choice is '+ computer_choice)
    return computer_choice

# PLAYER'S CHOICE

def player_selection(player_choice):
    choice_of_player = True
    while(choice_of_player):
        if (player_choice != 'R' and player_choice != 'S' and player_choice != 'P'):
            print('Invalid option. Please try again.... choose R, P or S')
            player_choice = input('Pick your choice: ')
            player_choice = player_choice.upper()
        else:
            print('Player\'s choice is '+ player_choice)
            choice_of_player = False
            return player_choice

# TIE GAME

def tie_game_checker(player_choice, computer_choice):
    if(player_choice == 'R' and computer_choice == 'R'):
        return (print("It's a TIE"))
        
    elif(player_choice == 'P' and computer_choice == 'P'):
        return (print("It's a TIE"))
    elif(player_choice == 'S' and computer_choice == 'S'):
        return (print("It's a TIE"))

# PLAYER WINS

def player_wins(player_choice, computer_choice):
    if(player_choice == 'R' and computer_choice == 'S'):
        return(print("You WIN!"))
    elif(player_choice == 'P' and computer_choice == 'R'):
        return(print("You WIN!"))
    elif(player_choice == 'S' and computer_choice == 'P'):
        return(print("You WIN!"))
    
#   COMPUTER WINS

def computer_wins(player_choice, computer_choice):
    if(player_choice == 'S' and computer_choice == 'R'):
        return(print("You LOSE!"))
    elif(player_choice == 'R' and computer_choice == 'P'):
        return(print("You LOSE!"))
    elif(player_choice == 'P' and computer_choice == 'S'):
        return(print("You LOSE!"))



while(game_on): 

   
    for i in range(1, 4): 

        print('\nRound', i, '\n')
        print('Begin!!!!')
        player_choice = input(
            "Pick your choice:\n'R' for Rock\n'P' for Paper\n'S' for Scissors\nSelect one: ")
        player_choice = player_choice.upper()
        player_choice = player_selection(player_choice)
        computer_choice = random_selection()

        # INVOKING THE FUNCTIONS

        player_win_the_game = player_wins(player_choice, computer_choice)
        computer_win_the_game = computer_wins(player_choice, computer_choice)
        tie_game = tie_game_checker(player_choice, computer_choice)

        # CHECK WINNER

        if(player_win_the_game):
            print(player_wins)
        elif(computer_win_the_game):
            print(computer_wins)
        elif(tie_game):
            print(tie_game)
    game_on = False
    
print("Thanks for playing the Rock-Paper-Scissors Game. BYE!!!..............SEE YOU NEXT TIME")