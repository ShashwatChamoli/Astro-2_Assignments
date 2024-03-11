import numpy as np
import matplotlib.pyplot as plt

# constants
sigma = 5.67e-8
alpha_0 = 0.1 # Assuming
sigma_0 = 0.2 # Assuming
L = 1 # Assuming

# Energy flux
# Part i
def F_i(r, T):
    return -16*sigma*(T**3)*(900/L)/(3*(alpha_0 + sigma_0)*r**(2))

# Part ii
def F_ii(r, T):
    return -16*sigma*(T**3)*(900/L)/(3*(alpha_0 + sigma_0)*np.log(r))

T = np.arange(100, 1001, 100)

r = np.linspace(0.1*L, 0.98*L, 1000)
# Note : To visualize the plot better, I have used 0.98L instead of L

# i part
for i in range(len(T)):
    plt.plot(r, F_i(r, T[i]), label='Temperature = {} K'.format(T[i]))

plt.legend()
plt.xlabel('Distance (r)')
plt.ylabel('Energy Flux')
plt.title('Energy Flux vs. Distance for Different Temperatures')
plt.show()

# ii part
for i in range(len(T)):
    plt.plot(r, F_ii(r, T[i]), label='Temperature = {} K'.format(T[i]))

plt.legend()
plt.xlabel('Distance (r)')
plt.ylabel('Energy Flux')
plt.title('Energy Flux vs. Distance for Different Temperatures')
plt.show()