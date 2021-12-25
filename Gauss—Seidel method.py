# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:58:40 2021

@author: Korkut Emre Arslantürk Number: 250206039
"""
## Note: I did this program using spyder from anaconda navigator.

#Define tolerance limits, initial values and iteration
tol_lim1 = 0.01; tol_lim2 = 0.001; tol_lim3 = 0.0001;
x_in= 0.0; y_in = 0.0; z_in = 0.0; iteration_1= 1;iteration_2= 1;iteration_3= 1;


# We have to define equations in diagonally dominant form to get correct results. 

func_1 = lambda x,y,z: (15+(1.8*y)-(2.2*z))/7.5
func_2 = lambda x,y,z: (18-(2*x)-(2.4*z))/(-9)
func_3= lambda x,y,z: (22-(1.6*x)+(4.2*y))/(-8)


#Gauss Seidel Iteration part1  E=0.01
print('Part 1 for ε=0.01\n')
print('Iteration\tX\tY\tZ\n')

#define error values just to do while loop i give them random but they must be bigger than tolerance limits.
e1=5; e2=5; e3=5
while (e1>tol_lim1 and e2>tol_lim1 and e3>tol_lim1):
    x1 = func_1(x_in,y_in,z_in)
    y1 = func_2(x1,y_in,z_in)
    z1 = func_3(x1,y1,z_in)
    print('%d\t%0.6f\t%0.6f\t%0.6f\n\n' %(iteration_1, x1,y1,z1))
    e1 = abs(x_in-x1); e2 = abs(y_in-y1); e3 = abs(z_in-z1);
    iteration_1 =iteration_1 + 1
    x_in = x1; y_in = y1; z_in = z1
    
    
print('Solution: x=%0.6f, y=%0.6f, z=%0.6f, iteration=%d\n'% (x1,y1,z1,iteration_1-1) )

#Gauss Seidel Iteration part2  E=0.001
print('Part 2 for ε=0.001\n')
print('Iteration\tX\tY\tZ\n')
#reset values
x_in1= 0.0; y_in1 = 0.0; z_in1 = 0.0;


e1=5; e2=5; e3=5
while (e1>tol_lim2 and e2>tol_lim2 and e3>tol_lim2):
    x2 = func_1(x_in1,y_in1,z_in1)
    y2 = func_2(x2,y_in1,z_in1)
    z2 = func_3(x2,y2,z_in1)
    print('%d\t%0.6f\t%0.6f\t%0.6f\n\n' %(iteration_2, x2,y2,z2))
    e1 = abs(x_in1-x2); e2 = abs(y_in1-y2); e3 = abs(z_in1-z2);
    
    iteration_2= iteration_2 + 1
    x_in1 = x2; y_in1 = y2; z_in1 = z2
    

print('Solution: x=%0.6f, y=%0.6f, z=%0.6f, iteration=%d\n'% (x1,y1,z1,iteration_2-1))

#Gauss Seidel Iteration part3  E=0.0001
print('Part 3 for ε=0.0001 \n')
print('Iteration\tX\tY\tZ\n')
#reset values
x_in2= 0.0; y_in2 = 0.0; z_in2 = 0.0;
e1=5; e2=5; e3=5
while (e1>tol_lim3 and e2>tol_lim3 and e3>tol_lim3):
    x3 = func_1(x_in2,y_in2,z_in2)
    y3 = func_2(x3,y_in2,z_in2)
    z3 = func_3(x3,y3,z_in2)
    print('%d\t%0.6f\t%0.6f\t%0.6f\n' %(iteration_3, x3,y3,z3))
    e1 = abs(x_in2-x3); e2 = abs(y_in2-y3); e3 = abs(z_in2-z3);
    iteration_3=iteration_3 + 1
    x_in2 = x3 ; y_in2 = y3; z_in2 = z3
    

print('\nSolution: x=%0.6f, y=%0.6f,  z=%0.6f, iteration=%d\n'% (x3,y3,z3,iteration_3-1))

