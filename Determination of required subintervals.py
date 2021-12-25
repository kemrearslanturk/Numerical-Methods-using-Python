# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 16:50:51 2021

@author: Korkut Emre Arslantürk/ 250206039
"""

# Note: I did this program using spyder from anaconda navigator.
#Please make sure you have installed python library for symbolic mathematics "sympy".

#Importing libraries
 
#%%
import sympy as sym
import math
import numpy as np
from sympy.utilities.lambdify import lambdify
 
# create a "symbol" called x
x = sym.Symbol('x')

#define values
a = np.pi / 6; b = np.pi / 2; error = 0.00001; 
dt=np.pi/3000;
t=np.linspace(a, b, num=1001)


#Define function
f=(sym.cos(x) * (sym.exp(x) + x)) / ((x * x) - sym.log(x))

# I found Exact Result using python integral function. In last part 
#I make error calculation using that.
from scipy.integrate import quad

def integrand(x):
    return (np.cos(x) * (np.exp(x) + x)) / ((x * x) - np.log(x))

ans, err = quad(integrand, a, b)
exact=ans

#Evaulating 2nd and 4th order Derivatives for using to find subinterval number
#according to error bound formulas.
derivative_f = f.diff(x,2) ; derivative_4f = f.diff(x,4)

#transform the function to available passing x values
f2order = lambdify(x,derivative_f); f4order = lambdify(x,derivative_4f)
forder=lambdify(x,f)
#Let me find K2 and K4 values which values give us max value for second and 
#4th order derivates. I need this according to Error bound formulas to find 
#compound midpoint, trapezoidal and Simpson's Method

dev2=np.zeros(1001)
j=1

while j<(len(t)-1):
    
        dev2[j]= f2order(j*dt)

        j=j+1


K2=max(abs(dev2))


dev4=np.zeros(1001)
j=1
while j<(len(t)-1):
    
        dev4[j]= f4order(j*dt)

        j=j+1



K4=max(abs(dev4))

#After find K2 and K4 values, I determine the number of subintervals required 
#for the compound midpoint, compound trapezoidal and Simpson’s to assure 
#this accuracy.

n_midpoint=pow(((K2*(pow((b - a),3)))/((abs(error) * 24))),1 / 2)
n_midpoint=math.ceil(n_midpoint)


n_trapezoidal=pow(((K2*(pow((b - a),3)))/(abs(error)*12)),1 / 2)
n_trapezoidal=math.ceil(n_trapezoidal)

n_simpson=pow(((K4*(pow((b - a),5)))/(abs(error)*180)),1 / 4);
n_simpson=math.ceil(n_simpson)


#I printed the number of subintervals required for the compound 
# midpoint, compound trapezoidal and Simpson’s to assure this accuracy.
print("Number of subintervals required for the compound midpoint ",n_midpoint)
print("Number of subintervals required for the compound trapezoidal ",n_trapezoidal)
print("Number of subintervals required for the Simpson's ",n_simpson)

#After that I found the results by using this subintervals and methods
#to prove that I was at the specified error

#Firstly, I found needed H values.
h_n=(b - a)/n_midpoint
h_t=(b - a)/n_trapezoidal
h_s=(b - a)/n_simpson

#Approximation according to compound midpoint
k = a + (h_n) / 2
res_1 = 0; i = 1
while i < (n_midpoint):
    
       d=(np.cos(k) * (np.exp(k) + (k)))/(((k) * (k)) - np.log(k))
       res_1 = d + res_1
       i = i + 1
       k = k + (h_n)


midpoint=h_n*res_1;
midpoint_error= ((abs(midpoint-exact))/exact)

#Approximation according to compound trapezoidal

i=1
res_2=0
while i<(n_trapezoidal):
    
       d=(np.cos(a+i*h_t)*(np.exp(a+i*h_t)+(a+i*h_t)))/(((a+i*h_t)*(a+i*h_t))-np.log(a+i*h_t))
       res_2=d+res_2
       i=i+1
       
fa=(np.cos(a)*(np.exp(a)+a))/((a*a)-np.log(a)); fb=(np.cos(b)*(np.exp(b)+b))/((b*b)-np.log(b))
res_2=res_2+(0.5*(fa + fb))
Trapezoidal=h_t*res_2
Trapezoidal_error= ((abs(Trapezoidal-exact))/exact)

#Approximation according to Simpson's Rule

m= np.linspace(a, b, n_simpson)

f_simp=(np.cos(m)*(np.exp(m)+m))/((m*m)-np.log(m))


firstpart=0; secondpart=0
i=1
while(i<=n_simpson-1):
    firstpart=firstpart+forder(a+i*h_s)
    i=i+2
    
    
    
i=2
while(i<=n_simpson-2):
    secondpart=secondpart+forder(a+i*h_s)
    i=i+2
    
result_simpson= (h_s/3)*(forder(a)+forder(b)+4*firstpart+2*secondpart)

simpson_error= ((abs(result_simpson-exact))/exact)

print("Exact Result",exact)
print("Midpooint Result: ",midpoint)
print("Trapezoidal Result",Trapezoidal)
print("Simpson Result: ",result_simpson)
print("Error of Midpoint: ",midpoint_error)
print("Error of Trapezoidal", Trapezoidal_error)
print("Error of Simpson Method:", simpson_error)