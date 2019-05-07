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

MAX_FV = 341

def simulateFriendship():
    """
        Runs the friendship simulation
    """
    p=""
    while p not in personality.personalities:
        p = input("Enter the first person's personality:").lower()
        if p not in personality.personalities:
            print("INVALID PERSONALITY")
    f1 = f.person(p)
    
    while p not in personality.personalities:
        p = input("Enter the first person's personality:").lower()
        if p not in personality.personalities:
            print("INVALID PERSONALITY")
    f2 = f.person(p)
    
    #TIME INVESTMENT IN HOURS
    inv=-1
    while inv<0 or inv>10:
        inv = int(input("Enter their time investment in hours per week (0-10):"))
        if inv<0 or inv>10:
            print("INVALID TIME INVESTMENT")
    #CONVERT TO MINUTES
    inv = inv*60
    
    #LENGTH FROM 0-100, 100 BEING THE LONGEST LASTING FRIENDSHIP
    l = -1
    while l<0 or l>100:
        l = int(input("Current length of friendship: "))
        if l<0 or l>100:
            print("INVALID PERSONALITY")
    
    #DISTANCE VALUE, ENTER VALUE CLOSEST
    d = -1
    while d>6 or d<1:
        print("How close do the friends live to each other? Input the number that matches the closest value.")
        print("Same City: 1")
        print("Same County: 2")
        print("Same State: 3")
        print("Same Country: 4")
        print("Same Continent: 5")
        print("Same Planet: 6")
        d = int(input())
        if d>6 or d<1:
            print("INVALID DISTANCE NUMBER")
    
    friendship = f.friendship(f1,f2,inv,l,d)
    simulation_length = friendship.getRemaining()
    msg = ""
    for i in range(simulation_length):
        hardship = random.randint(0,MAX_FV)
        fv = friendship.getFV()
        if hardship>fv:
            friendship.friends = False
            msg = "Friendship did not survive hardship, lasted " + str(friendship.getLOF()) + " years.\n"
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
    