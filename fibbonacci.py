# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 16:29:01 2022

@author: Wakchaure Ishwari Dnyaneshwar
"""

#fibonnacci numner

def fib(n):
    n1=0
    n2=1
    print(n1,"\n",n2)
    for i in range(2,n):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
    
fib(6)

def fib(n):
    if(n<=1):
        return(n)
    else:
        return(fib(n-1)+fib(n-2))
n=int(input("ENter no of terms: "))       
for i in range(n):
    print(fib(i))
    
    