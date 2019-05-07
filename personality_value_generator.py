# -*- coding: utf-8 -*-
"""
@author:
    Kathryn Saldivar    108578476
    Dulce Meza-Flores   109754287
    Elizabeth-Agnes Gaw 109232948
    
RESULTS:
"""
import pandas as pd
from mlxtend.preprocessing import minmax_scaling

ISTP = pd.Series([5,4,2,1], index=(range(4)))
INFJ = pd.Series([4,3,1], index=(range(3)))
ISTJ = pd.Series([6,4,3,2,1], index=(range(5)))
ISFP = pd.Series([4,3,2,1], index=(range(4)))
ISFJ = pd.Series([7,2,1], index=(range(3)))
INTJ = pd.Series([5,3,2,1], index=(range(4)))
INTP = pd.Series([4,3,2,1], index=(range(4)))
INFP = pd.Series([2,1], index=(range(2)))

ENFP = pd.Series([5,4,3,2,1], index=(range(5)))
ESFP = pd.Series([3,2,1], index=(range(3)))
ENTJ = pd.Series([4,3,2,1], index=(range(4)))
ENTP = pd.Series([5,4,3,2,1], index=(range(5)))
ENFJ = pd.Series([6,4,2,1], index=(range(4)))
ESFJ = pd.Series([6,3,2,1], index=(range(4)))
ESTJ = pd.Series([3,2,1], index=(range(3)))
ESTP = pd.Series([3,2,1], index=(range(3)))

df1 = pd.DataFrame(ISTP, columns=['ISTP'])
df2 = pd.DataFrame(INFJ, columns=['INFJ'])
df3 = pd.DataFrame(ISTJ, columns=['ISTJ'])
df4 = pd.DataFrame(ISFP, columns=['ISFP'])
df5 = pd.DataFrame(ISFJ, columns=['ISFJ'])
df6 = pd.DataFrame(INTJ, columns=['INTJ'])
df7 = pd.DataFrame(INTP, columns=['INTP'])
df8 = pd.DataFrame(INFP, columns=['INFP'])

df9 = pd.DataFrame(ENFP, columns=['ENFP'])
df10 = pd.DataFrame(ESFP, columns=['ESFP'])
df11 = pd.DataFrame(ENTJ, columns=['ENTJ'])
df12 = pd.DataFrame(ENTP, columns=['ENTP'])
df13 = pd.DataFrame(ENFJ, columns=['ENFJ'])
df14 = pd.DataFrame(ESFJ, columns=['ESFJ'])
df15 = pd.DataFrame(ESTJ, columns=['ESTJ'])
df16 = pd.DataFrame(ESTP, columns=['ESTP'])



print(minmax_scaling(df1, columns=['ISTP']))
print(minmax_scaling(df2, columns=['INFJ']))
print(minmax_scaling(df3, columns=['ISTJ']))
print(minmax_scaling(df4, columns=['ISFP']))
print(minmax_scaling(df5, columns=['ISFJ']))
print(minmax_scaling(df6, columns=['INTJ']))
print(minmax_scaling(df7, columns=['INTP']))
print(minmax_scaling(df8, columns=['INFP']))

print(minmax_scaling(df9, columns=['ENFP']))
print(minmax_scaling(df10, columns=['ESFP']))
print(minmax_scaling(df11, columns=['ENTJ']))
print(minmax_scaling(df12, columns=['ENTP']))
print(minmax_scaling(df13, columns=['ENFJ']))
print(minmax_scaling(df14, columns=['ESFJ']))
print(minmax_scaling(df15, columns=['ESTJ']))
print(minmax_scaling(df16, columns=['ESTP']))

