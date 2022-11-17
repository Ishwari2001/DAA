# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 16:55:08 2022

@author: Wakchaure Ishwari Dnyaneshwar
"""

def fractionalknapsack(values,weights,Total_capacity):
    n = len(values)

    def score(i) : 
        return values[i]/weights[i]

    items = sorted(range(n)  , key=score , reverse = True)
    
    sel, value,weight = [],0,0
    for i in items:
        if weight +weights[i] <= capacity:
            sel += [i]
            weight += weights[i]
            value += values [i]
    return value


values=[120,60,100]
weights=[30,20,50]
capacity=60
print(fractionalknapsack(values, weights,capacity))