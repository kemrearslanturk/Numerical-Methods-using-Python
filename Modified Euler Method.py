# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 14:58:24 2021

@author: Korkut Emre Arslantürk/ 250206039
"""
# Note: I did this program using spyder from anaconda navigator.
#Please make sure you have installed python library for symbolic mathematics "sympy".

#Importing libraries

import sympy as sym

# create a "symbol" called x and y
x, y = sym.symbols('x y')

#define values
h= 0.0001;  x_0=0; u_0=2; x_1=0; n=1

#Define function
f= 0.5*(1+x)*y*y

#make it function valuable
f_val=sym.lambdify([x, y], f)

#Applying Modified Euler Method 

while (x_0<=0.2-h):
    u1_pred= u_0 + h*f_val(x_0,u_0)
    x_1=x_0+h
    u1_cor=u_0 +(h/2)*(f_val(x_0,u_0)+f_val(x_1,u1_pred))
    x_0=x_1
    if(n==1 or n==2000):##because of first term and last term desired I print just them.
        print("U%d = %f"%(n,u1_cor))
    u_0=u1_cor
    n=n+1;






    