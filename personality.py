# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:35:58 2019

@author:
    Kathryn Saldivar    108578476
    Dulce Meza-Flores   109754287
    Elizabeth-Agnes Gaw 109232948
"""
personalities = ["istj","istp","infj","enfj","enfp","entj","intp","estp","intj","esfp","entp","isfj","estj","esfj","isfp","infp"]

p_dict = {
        "istj":{"intj":40,"entj":27,"esfj":18,"istp":18,"isfj":18,"estj":9,"intp":5,"ispj":5},
        "istp":{"intj":45,"infj":37,"infp":37,"esfj":12,"isfj":12,"intp":12,"isfp":12,"istj":5,"enfj":5,"esfp":5,"entj":5,"enfp":5,"entp":5},
        "infj":{"infp":53,"intj":40,"esfj":6,"enfp":6,"isfj":6,"enfj":6,"entp":6,"intp":6,"istp":6},
        "enfj":{"esfj":50,"esfp":50,"isfj":33,"isfp":11,"entj":11,"estj":11,"infj":5,"istp":5,"intp":5},
        "enfp":{"estp":36,"enfj":30,"esfj":20,"infp":20,"entp":20,"isfj":10,"esfp":10,"isfp":4},
        "entj":{"esfj":45,"isfj":45,"estj":33,"istp":16,"isfp":16,"intp":5,"esfp":5,"enfj":5,"entp":5,"istj":5},
        "intp":{"intj":45,"isfp":33,"istp":16,"entp":16,"infp":16,"intp":5,"estp":5,"isfj":5,"infj":5,"entj":5},
        "estp":{"entp":60,"entp":60,"estj":33,"esfp":33,"entj":33,"istp":6,"infj":6,"isfp":6},
        "intj":{"infp":51,"istp":28,"entp":28,"isfp":14,"istj":5,"estj":5,"entj":5,"infj":5,"intp":5},
        "esfp":{"estp":60,"enfj":33,"esfj":33,"entp":6,"entj":6,"isfj":6,"isfp":6,"enfp":6,"estj":6,"istp":6},
        "entp":{"esfp":36,"enfj":10,"entj":10,"enfp":10,"estp":10,"intr":10,"intj":10,"isfp":4,"istp":4,"estj":4},
        "isfj":{"istj":76,"isfj":14,"intj":14,"esfj":14,"estj":14,"isfp":9,"esfp":9,"enfj":9,"infj":9,"istp":9},
        "estj":{"esfj":60,"enfj":60,"istj":60,"entj":33,"esfp":33,"estp":33,"intj":6,"entp":6},
        "esfj":{"isfj":56,"enfj":25,"isfp":25,"esfj":25,"esfp":12,"infj":12,"istj":6,"intp":6,"istp":6},
        "isfp":{"esfj":45,"isfj":33,"intj":16,"entp":16,"infp":16,"estp":5,"esfp":5,"intp":5,"istp":5,"enfp":5,"enfj":5},
        "infp":{"intj":90,"infj":90,"esfj":10,"intp":10,"istp":10,"entp":10,"isfp":10,"istj":10}
        }

def getPV(p1,p2):
    """
        Returns the Friendship Value for two personalities.
        Personalities should be a string matching with a personality in the Myers-Briggs personality model.
    """
    p1 = p1.lower()
    p2 = p2.lower()
    if p1 not in personalities or p2 not in personalities:
        print("INVALID PERSONALITY")
    #IF A FRIENDSHIP VALUE EXISTS IT RETURNS THE VALUE, ELSE IT RETURNS 1
    vals = p_dict[p1]
    if p2 in vals.keys(): #key exists
        return 2*vals[p2]
    else:
        return 2