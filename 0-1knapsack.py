# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 17:09:09 2022

@author: Wakchaure Ishwari Dnyaneshwar
"""

def knapsack01(W,N,v,w) :
    DP =[]
    for i in range(W+1):
        DP.append(0)

    for i in range(1,N+1) :
        for j in range(W,w[i-1]-1,-1) :
               
                DP[j] = max(v[i-1]+DP[j-w[i-1]],DP[j]) 
   
    return DP[W]

n=4
W=25
v=[10,12,14,16]
w=[9,8,12,14]
print(knapsack01(W, n, v, w))
