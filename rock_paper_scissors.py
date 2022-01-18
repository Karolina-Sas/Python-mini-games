# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:48:33 2020

@author: PC
"""

import random 
import sys
random_number=random.random() 


while True:
    
    choice=input("Choose Rock, Paper, Scissors, Lizard or Spock: ")
    if choice=="Lizard" or choice=="Scissors" or choice=="Paper" or choice=="Rock" or choice=="Spock":
        break        
    if choice=="q":
        sys.exit()
    else:
        print("Incorrect input, try again")
                     
    
if 0<random_number<=0.2:
    print("Computer has chosen Rock")
    if choice=="Rock":
        print("Draw!")
        
    elif choice=="Lizard" or choice=="Scissors":
        print("You lost. Rock crushes", choice)
        
    elif choice=="Paper":
        print("You win. Paper covers rock")
        
    elif choice=="Spock":
        print("You win. Spock vaporizes rock")

            
elif 0.2< random_number<=0.4:
    print("Computer has chosen Paper")
    if choice=="Paper":
         print("Draw!")
    elif choice=="Rock":
        print("You lost. Paper covers rock")
    elif choice=="Spock":
        print("You lost.Paper disproves spock")
    elif choice=="Lizard":
        print("You win. Lizard eats paper")
    elif choice=="Scissors":
        print("You win.Scissors cuts paper")
   
elif 0.4< random_number<=0.6:
    print("Computer has chosen Scissors")
    if choice=="Scissors":
        print("Draw!")
    elif choice=="Paper":
        print("You lost. Scissors cuts paper.")
    elif choice=="Lizard":
        print("You lost. Scissors decapitates lizard.")
    elif choice=="Spock":
        print("You win. Spock smashes lizard.")
    elif choice=="Rock":
        print("You win. Rock crushes scissors")
   
elif 0.6< random_number<=0.8:
    print("Computer has chosen Lizard")
    if choice=="Lizard":
        print("Draw!")
    elif choice=="Spock":
        print("You lost.Lizard poisons spock")
    elif choice=="Paper":
        print("You lost. Lizard eats paper.")
    elif choice=="Scissors":
        print("You win. Scissors decapitates lizard.")
    elif choice=="Rock":
        print("You win. Rock crushes lizard.")
   
else:
    print("Computer has chosen Spock")
    if choice=="Spock":
        print("Draw!")
