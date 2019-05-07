# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:27:42 2019

@author: Dulce

RESULTS: The highest time invest value achievable is 210 and the lowest is 0
The final_value list generates a list of values, each run is different becuase the 
number of activites is always different for each run
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

activity_num = 0
time_value = 0
#read the cvs file and only look at time invested per week 
data = pd.read_csv("survey.csv", delimiter = ',')
article_read = data
#a list with the number of responses 
resp_number = []
#time invested in minutes list
time_invest_min = []
frequency_min = 0
#activity number list
activity_rand = []
#random activity, set in stone
activity=[27, 16, 9, 0, 35, 19, 32, 
          23, 16, 31, 10, 2, 28, 18, 
          35, 25, 6, 26, 29, 27, 34, 
          6, 28, 6, 37, 23, 13, 19, 
          35, 25, 38, 11, 36, 16, 28,
          9, 30, 10, 38, 23, 27, 35, 
          1, 9, 36, 8, 0, 29, 33, 36, 
          10, 13, 23, 32, 37, 35, 14, 
          14, 36, 23, 0]
for k in activity:
    print(k)
#normalized final vlaues, all add up to 1
norm_time =[]
#final value list
final_value = []
#add indices to responses list 
for response in range(61):
    resp_number.append(response)

#highest possible time value
time_vals = []
for time_val in range(61):
    time_vals.append(time_val)

def hour_to_min():
    """convert collected data from hours to minutes, if we have a range like x -y 
    I will find the range of the value by largest minus smallest"""
    for x in range(len(resp_number)):
        frequency_min = article_read["Range"][x] * 60
        time_invest_min.append(frequency_min)
    
    print("Time in min list ",time_invest_min, "\n")

        
hour_to_min()       


def generate_rand_activity():
    
    """ to simulate the diversity (# of activities) that are done together we will 
    generate a random value from 0 to 38 this is according to the 
    The Common Cold Project - Relationship Closeness by Carnegie Mellon  """
    for x in range(61):
        activity_num = random.randint(0,38)
        activity_rand.append(activity_num)
    
    print ("activity List", activity_rand, "\n")

#only run once 
#generate_rand_activity()
    
def add_weight():
    """we will weight the time value since it is not about how much time 
    you spend but what you do with the time, highest is 210, and lowest is 0 """
    for x, y in zip(activity, time_invest_min):
        if 0 <= x <= 3:
            time_value = .05 * y
            final_value.append(time_value)
           
        elif 4 <= x <= 9:
            time_value = .15 * y
            final_value.append(time_value)
            
        elif 10 <= x <= 18:
            time_value = .20 * y
            final_value.append(time_value)
            
        elif 19 <= x <= 30:
            time_value = .25 * y
            final_value.append(time_value)
            
        elif 30 <= x <= 38:
            time_value = .35 * y
            final_value.append(time_value)
        else:
            print("Could not add wieghts")
            
    
    print("Final Values", final_value)
  
    
add_weight()


def normalize():
    """Normalize each value to add up to 1"""
final_sum=sum(final_value)
for j in activity:
    norm = j/final_sum
    norm_time.append(round(norm, 4))
print ("normalized Time Invested", norm_time)




normalize()

#plot the final values
plt.hist(final_value, rwidth=.9, density=False, label = ['Time Invested Weighted Value'])
plt.legend()
plt.xlabel("Time Invested Value")
plt.ylabel("# of occurences")
plt.title("Histogram of Time Invested Value")

# naming the x axis 
#plt.xlabel('Final Time Invested Value ') 
# naming the y axis 
#plt.ylabel('Time Invested')
#plt.plot( time_vals, time_invest_min)
#plt.show()

