import numpy as np
import matplotlib.pylab as plt
import math as m

n = np.arange(0,199)
xa = (input('Give an equation to evaluate n:'))   
 
def x(n):       
    w=eval(xa)  
    return w

for N in n:     
    if N == 0:
        y = -1.5*x(n) + 2*x(n+1) - 0.5*x(n+2)
    elif N > 0 and N <= 198:
        y = 0.5*x(n+1) - 0.5*x(n-1)
    else:
        y = 1.5*x(n) - 2*x(n-1) + 0.5*x(n-2)

plt.plot(x(n),color='c', label = 'Function of x(n)')    
plt.plot(y,color='m', label = 'Function of y(n)')       
plt.legend()
plt.grid()
plt.xlabel('The range of n numbers to 200:')
plt.ylabel('Value of x(n) and y(n):')
plt.show()