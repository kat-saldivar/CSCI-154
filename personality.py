# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:35:58 2019

@author:
    Kathryn Saldivar    108578476
    Dulce Meza-Flores   109754287
    Elizabeth-Agnes Gaw 109232948
"""
personalities = ["istj","istp","infj","enfj","enfp","entj","intp","estp","intj","esfp","entp","isfj","estj","esfj","isfp","infp"]
def getPV(p1,p2):
    """
        Returns the Friendship Value for two personalities.
        Personalities should be a string matching with a personality in the Myers-Briggs personality model.
    """
    p1 = p1.lower()
    p2 = p2.lower()
    if p1 not in personalities or p2 not in personalities:
        print("INVALID PERSONALITY")
    #TODO input full personality chart