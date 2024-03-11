import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp

# Question 2 (i) part

def dI_i(r, I_nu):
    return -(I_nu*r) + (1/r**2)

def dI_ii(r, I_nu):
    return -I_nu*r*np.exp(-r/L) + np.log(r/L)

L = 1 # Assuming
r = np.linspace(0.1*L, L, 1000)
I_nu_0 = [100]

sol_i= solve_ivp(dI_i, [0.1*L, L], I_nu_0, t_eval=np.linspace(0.1*L, L, 100))
sol_ii = solve_ivp(dI_ii, [0.1*L, L], I_nu_0, t_eval=np.linspace(0.1*L, L, 100))

plt.plot(sol_i.t, sol_i.y[0])
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity vs r (Part i)')

plt.plot(sol_ii.t, sol_ii.y[0])
plt.xlabel('r')
plt.ylabel('Intensity')
plt.title('Intensity vs r (Part ii)')

plt.legend(['part a', 'part b'])
plt.show()