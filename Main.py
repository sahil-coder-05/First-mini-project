'''
1 for snake

-1 for water

0 for gun

'''
#Import random module
import random

computer = random.choice ([1 , -1 , 0])

player = input('''Enter you choice  \ns for sanke: \nw for water: \ng for gun  :  ''')

player_dict = {"s": 1 , "w": -1 , "g": 0}

computer_dict = {1: "snake", -1:"water", 0:"gun"}

player_choice = player_dict[player]

print(f"You choose {computer_dict[player_choice]}\nComputer choose {computer_dict[computer]}")

if (computer == player_choice):
    print("Its a draw")

else:
    
    if(computer == 1  and player_choice == -1):
        print("Shittt!! You lose!")
    
    elif(computer == 1 and player_choice == 0):
        print("Wooo!! You win!!")
        
    elif(computer == -1  and player_choice == 1):
        print("Wooo!! You win!!")
    
    elif(computer == -1 and player_choice == 0):
        print("Shittt!! You lose!")
         
    elif(computer == 0  and player_choice == 1):
        print("Shittt!! You lose!") 
    
    elif(computer == 0 and player_choice == -1):
        print("Wooo!! You win!!")
       
    else:
        print("Something went wrong, Please try again!!")
       


