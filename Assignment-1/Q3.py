import numpy as np
import matplotlib.pyplot as plt 

L = 1    #Assuming length of the system to be 1m
T = 500

def optical_depth(part, r, L):
    if (part == 1):
        return (r*r)/2
    elif (part == 2):
        return L**2 - (L*r + L**2)*np.exp(-r/L)

# Initial values 
T_b0 = [100, 10000]

def T_b(r, L, part, T_b0, T):
    return T_b0*np.exp(-optical_depth(part, r, L)) + T*(1 - np.exp(-optical_depth(part, r, L)))

x = np.linspace(0.1, 1, 1000)

# Multiply each element of the array by L
r = x * L

# (i) part
plt.plot(r, T_b(r, L, 1, T_b0[0], T))
plt.plot(r, T_b(r, L, 2, T_b0[0], T))
plt.ylabel('Brightness Temperature(in K)')
plt.xlabel('r(in m)')
plt.title('Brightness Temperature for L = 1m (T_b(0) = {}K)'.format(T_b0[0]))
plt.legend(['part (a) of Q2', 'part (b) of Q2'])
plt.show()

# (ii) part
plt.plot(r, T_b(r, L, 1, T_b0[1], T))
plt.plot(r, T_b(r, L, 2, T_b0[1], T))
plt.ylabel('Brightness Temperature(in K)')
plt.xlabel('r(in m)')
plt.title('Brightness Temperature for L = 1m (T_b(0) = {}K)'.format(T_b0[1]))
plt.legend(['part (a) of Q2', 'part (b) of Q2'])
plt.show()


