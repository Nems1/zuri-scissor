#Import os to access operating system commands

import os 

# Import random to access choice() methos

import random

cpu = random.choice(['P','R','S']) # cpu stands for computer

# Loop to allow player make a choice to play again or 

while True:
    # Clear console screen (here windows environmnet

    os.system('clear')  # on Windows use os.systm('cls')
    
    #Get Player choice and convert it to upper case

    player = input('\n\tMake your choice (P->Paper,R-> Rock,S->Scissor) :').upper()

    # Check if player choice is a  valid one

    if player in ('P','R','S'):
    
        #Compare Player choice and that of computer
    
        if player == cpu :
            print(f'\n\tPlayer({player}) : CPU ({cpu}).There is a tie')
        elif player == 'P' and cpu == 'R':
            print(f'\n\tPlayer({player}) : CPU ({cpu}).You win')
        elif player == 'R' and cpu == 'S':
            print(f'\n\tPlayer({player}) : CPU ({cpu}).You win')
        elif player == 'S' and cpu == 'P':
            print(f'\n\tPlayer({player}) : CPU ({cpu}).You win')
        else:
            print(f'\n\tPlayer({player}) : CPU ({cpu}).You lose Computer WINS!')
    else:
    
        # Let player know s/he made a wrong chpice
    
        print(f'\n\tYour choice ({player}) is invalid.\n\tValid choices (P->Paper,R-> Rock,S->Scissor).Try again.')    

    play_again = input('\n\tPlayer again y/n? ').upper()        
    if play_again != 'Y':
        break
