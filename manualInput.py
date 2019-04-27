# -*- coding: utf-8 -*-
"""
user manual input

@author: 
    Kathryn Saldivar
    Dulce Meza-Flores
    Elizabeth-Agnes Gaw
"""

import friendship as f
import random

def simulateFriendship():
    """
        Runs the friendship simulation
    """
    print("Enter the first person's personality and time investment:")
    p = input("Personality: ")
    #TODO CHECK PERSONALITY VALUE
    t_i = input("Time Investment: ")
    #TODO CHECK TIME VALUE
    f1 = f.person(p,t_i)
    print("Enter the second person's personality and time investment:")
    p = input("Personality: ")
    #TODO CHECK PERSONALITY VALUE
    t_i = input("Time Investment: ")
    #TODO CHECK TIME VALUE
    f2 = f.person(p,t_i)
    
    l = int(input("Enter the starting length of time of the friendship in years: "))
    d = int(input("Enter the distance between where the friends live: "))
    #TODO CHECK LENGTH AND DISTANCE VALUES
    
    friendship = f.friendship(f1,f2,l,d)
    simulation_length = friendship.getRemaining()
    msg = ""
    for i in range(simulation_length):
        hardship = random.randint(0,100)
        #TODO INCORPORATE ACTUAL HARDSHIP VARIANCE
        if hardship>99:
            friendship.friends = False
            msg = "Friendship did not survive hardship, lasted " + str(friendship.getLOF()) + " years." 
            break
        friendship.oneMoreYear()
    if msg!="":
        msg = "Friendship successfully lasted forever!"
    print(msg)

def mainMenu():
    """
        Print the main commands.
    """
    print("Command List:")
    print("q: quit")
    print("n: run new friendship simulation")
    print("m: open command menu")
    
    
#MAIN PROGRAM    
c = "m"
while c!='q':
    if c=='m':
        mainMenu()
    elif c=='n':
        simulateFriendship()
    else:
        print("Invalid command. Input 'm' for list of commands.")
    c = input("Enter a Command: ")
    