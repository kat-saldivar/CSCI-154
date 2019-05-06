# -*- coding: utf-8 -*-
"""
user manual input

@author: 
    Kathryn Saldivar    108578476
    Dulce Meza-Flores   109754287
    Elizabeth-Agnes Gaw 109232948
"""

import friendship as f
import personality
import random

def simulateFriendship():
    """
        Runs the friendship simulation
    """
    print("Enter the first person's personality and time investment:")
    p=""
    while p not in personality.personalities:
        print("Enter the first person's personality and time investment:")
        p = input("Personality: ")
        if p not in personality.personalities:
            print("INVALID PERSONALITY")
    t_i = input("Time Investment: ")
    #TODO CHECK TIME VALUE
    f1 = f.person(p,t_i)
    
    while p not in personality.personalities:
        print("Enter the second person's personality and time investment:")
        p = input("Personality: ")
        if p not in personality.personalities:
            print("INVALID PERSONALITY")
    t_i = input("Time Investment: ")
    #TODO CHECK TIME VALUE
    f2 = f.person(p,t_i)
    
    l = int(input("Current length of friendship: "))
    d = -1
    while d<0:
        print("How close do the friends live to each other? Input the number that matches the closest value.")
        print("Same City: 1")
        print("Same County: 2")
        print("Same State: 3")
        print("Same Country: 4")
        print("Same Continent: 5")
        print("Same Planet: 6")
        d = int(input())-1
        if d>5 or d<0:
            print("INVALID NUMBER")
            d = -1
    #TODO CHECK LENGTH AND DISTANCE VALUES
    
    friendship = f.friendship(f1,f2,l,d)
    simulation_length = friendship.getRemaining()
    msg = ""
    for i in range(simulation_length):
        hardship = random.randint(0,100)
        #TODO INCORPORATE ACTUAL HARDSHIP VARIANCE
        if hardship>90:
            friendship.friends = False
            msg = "Friendship did not survive hardship, lasted " + str(friendship.getLOF()) + " years.\n"
            msg = msg + "Ended due to a level " + str(hardship) + " hardship."
            break
        friendship.oneMoreYear()
    if msg=="":
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
    