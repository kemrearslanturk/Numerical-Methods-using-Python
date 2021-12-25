# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 22:46:50 2021

@author: Korkut Emre Arslantürk / Number: 250206039
"""
# Note: I did this program using spyder from anaconda navigator.
#Please make sure you have installed python library for symbolic mathematics "sympy".

#Importing libraries
 

import sympy as sym
from sympy.utilities.lambdify import lambdify
 
# create a "symbol" called x
x = sym.Symbol('x')
#Define function
f=sym.exp(2*x)*sym.sin(x) - 3*x*sym.cos(2*x)

#Define derivative
derivative_f = f.diff(x,1) ;

#make it function and derivative valuable
f2order = lambdify(x,derivative_f);
forder=lambdify(x,f)

#define values
iteration=0; e1=0.001; e2=0.0001; e3=0.00001; guess=1.0

#Applying Newton's Method for e1=0.001
print('Part 1\n')
print('Iteration\tRoot\n')
while(forder(guess)>e1):
    
    newguess=guess- (forder(guess)/f2order(guess))
    guess=newguess
    iteration=iteration+1
    print('%d\t%0.6f\n\n' %(iteration, guess))
     
     
print("For tolerance limit: ",e1)
print("Root: ",guess)
print("Error= ",abs(forder(guess)))
print("Iteration number: ",iteration)
print("\n\n")


#Applying Newton's Method for e2=0.0001
guess=1.0
iteration=0

print('Part 2\n')
print('Iteration\tRoot\n')

while(forder(guess)>e2):
    
    newguess=guess- (forder(guess)/f2order(guess))
    guess=newguess
    iteration=iteration+1
    print('%d\t%0.6f\n\n' %(iteration, guess))
print("For tolerance limit: ",e2)
print("Root: ",guess)
print("Error= ",abs(forder(guess)))
print("Iteration number: ",iteration)
print("\n\n")


#Applying Newton's Method for e3=0.00001

guess=1.0
iteration=0
print('Part 3\n')
print('Iteration\tRoot\n')

while(forder(guess)>e3):
    
    newguess=guess- (forder(guess)/f2order(guess))
    guess=newguess
    iteration=iteration+1
    print('%d\t%0.6f\n\n' %(iteration, guess))
print("For tolerance limit: ",e3)
print("Root: ",guess)
print("Error= ",abs(forder(guess)))
print("Iteration number: ",iteration)


    

