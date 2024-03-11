import numpy as np
import matplotlib.pyplot as plt 

# Question 2 (ii) part
L = 1    #Assuming length of the system to be 1m


def optical_depth(part, r, L):
    if (part == 1):
        return (r**2)/2
    elif (part == 2):
        return L**2 - (L*r + L**2)*np.exp(-r/L)
    
x = np.linspace(0.1, 1, 1000)

# Multiply each element of the array by L
r = x * L

plt.plot(r, optical_depth(1, r, L))   # part (a)
plt.plot(r, optical_depth(2, r, L))   # part (b)
plt.ylabel('Optical depth')
plt.xlabel('r')
plt.title('Optical depth for L = 1m')
plt.legend(['part (a)', 'part (b)'])
plt.show()
    