import art
import random
from replit import clear
from game_data import data

def present_choice(size_list, last_choice) :

    if len(size_list) == 0 :
        print("You beat the game!\n")
        print(art.you_won)
        return [-1, -1]
    
    choice = random.choices(size_list, k = 2)
    size_list.remove(choice[1])
    
    if last_choice == -1 :
        size_list.remove(choice[0])
    else :
        choice[0] = last_choice
    
    print("Guess, who has more followers, 'a' or 'b'?:\n")
    print(f"'a' : {data[choice[0]]['name']}, {data[choice[0]]['description']} from {data[choice[0]]['country']}.")
    print(art.vs)
    print(f"'b' : {data[choice[1]]['name']}, {data[choice[1]]['description']} from {data[choice[1]]['country']}.\n")
    return choice

def higher_lower() :
    data_size_list = list(range(len(data)))

    continue_game = True
    current_score = 0
    last_option = -1
    player_guess = 'a'

    
    while continue_game :
        clear()
        print(art.logo)

        input_incorrect = True
        
        print(f"Your current score is {current_score}.\n")
    
        selection = present_choice(data_size_list, last_option)
        if selection[0] == -1 :
            return 0
        
        fate = data[selection[0]]['follower_count'] > data[selection[1]]['follower_count']
        
        while input_incorrect :
            input_incorrect = False
            
            player_guess = input("Input 'a' or 'b': ")
            if player_guess == 'a' :
                if fate :
                    current_score += 1
                    last_option = selection[0]
                else :
                    continue_game = False
            elif player_guess == 'b' :
                if not fate :
                    current_score += 1
                    last_option = selection[1]
                else :
                    continue_game = False
            else :
                input_incorrect = True
                print("Wrong choice, try again!")
                
                
    print(f"You guessed wrong, your final score is {current_score}!") 

    decision = input("To play again, type 'y'")
    if decision == 'y' :
        higher_lower()

higher_lower()