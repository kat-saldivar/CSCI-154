# -*- coding: utf-8 -*-
"""
friendship and person classes

@authors:
    Kathryn Saldivar    108578476
    Dulce Meza-Flores   109754287
    Elizabeth-Agnes Gaw 109232948
"""

import personality
import random

d_dict = {
        1 : 41,
        2 : 26,
        3 : 16,
        4 : 10,
        5 : 6,
        6 : 4
        }

class person:
    def __init__(self,p):
        """
            person(p,i)
            personality is a number that correlates to a table with the personality information
            investment is the number of hours a week the person is willing to invest in a relationship
        """
        self.personality = p
        
    def getPersonality(self):
        return self.personality
    
class friendship:
    def __init__(self,f1,f2,i,l=0,d=0):
        """
            friendship(f1,f2,l,d)
            f1 is the first person in a friendship
            f2 is the second person in a friendship
            l is the length of time they have been friends. Defaults to zero if doing a new friendship.
            d is the distance they live from each other simplifying by using a code number.
                0 = same city; 1 = same county; 3 = same state; 4 = same country; 5 = same continent; 6 = else
        """
        self.friends = True
        self.f1 = f1
        self.f2 = f2
        self.investment = i #IN MINUTES
        self.length_of_friendship = l
        self.remaining_time = 100-l
        self.distance = d
        print("DISTANCE: " + str(self.distanceFV))
        print("PERSONALITY: " + str(self.getPFV))
        self.calculateFV()
        
    def calculateFV(self):
        """
            Uses all the variables to create a number which determines how likely a friendship will survive hardship
        """
        fv = 0
        #ADD DISTANCE, PERSONALITY, LOF, AND TIME INVESTMENT
        fv = fv + self.distanceFV()
        fv = fv + self.getPFV()
        fv = fv + self.getTIFV()
        
        self.friendshipValue = fv
        
        
    def getFV(self):
        self.calculateFV()
        return self.friendshipValue
    
    def distanceFV(self):
        d = self.distance
        return d_dict[d]
    
    def getPFV(self):
        p1 = self.f1.getPersonality()
        p2 = self.f2.getPersonality()
        return personality.getPV(p1,p2)
    
    def getTIFV(self):
        time_value=0
        time = self.investment
        
        activity = random.randint(0,38) #RANDOM FROM 0-38
        
        if 0 <= activity <= 3:
            time_value = .05 * time
        elif 4 <= activity <= 9:
            time_value = .15 * time
        elif 10 <= activity <= 18:
            time_value = .20 * time
        elif 19 <= activity <= 30:
            time_value = .25 * time     
        elif 30 <= activity <= 38:
            time_value = .35 * time
        else:
            print("INVALID ACTIVITY INPUT")
            return 0
        print("TIME: " + str(time_value))
        return time_value
    
    def getRemaining(self):
        return self.remaining_time
    
    def getLOF(self):
        return self.length_of_friendship
    
    def oneMoreYear(self):
        self.length_of_friendship += 1
        self.remaining_time -= 1
       

