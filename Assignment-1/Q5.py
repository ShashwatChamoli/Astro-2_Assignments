import numpy as np
import matplotlib.pyplot as plt

# constants
alpha_0 = 0.1 # Assuming
sigma_0 = 0.2 # Assuming
I_0 = 1000 # Assuming
L = 1 # Assuming

# Part i
# Part a
def I_i(r):
    return I_0*np.exp(-(alpha_0 + sigma_0)*(r**3/3))
# Part b
def I_ii(r):
    return I_0*np.exp(-(alpha_0 + sigma_0)*(r*np.log(r) - r))

# Part ii
# Part a
def tau_i(r):
    return (alpha_0 + sigma_0)*(r**3/3)
# Part b
def tau_ii(r):
    return (alpha_0 + sigma_0)*(r*np.log(r) - r)

r = np.linspace(0.1*L, L, 1000)

plt.plot(r, I_i(r))
plt.title('Intensity vs distance(r) for r^2 dependence')
plt.ylabel('Intensity')
plt.xlabel('r')
plt.show()

plt.plot(r, I_ii(r))
plt.title('Intensity vs distance(r) for ln(r) dependence')
plt.ylabel('Intensity')
plt.xlabel('r')
plt.show()

plt.plot(r, tau_i(r))
plt.title('Optical depth vs distance(r) for r^2 dependence')
plt.ylabel('Optical depth')
plt.xlabel('r')
plt.show()

plt.plot(r, tau_ii(r))
plt.title('Optical depth vs distance(r) for ln(r) dependence')
plt.ylabel('Optical depth')
plt.xlabel('r')
plt.show()

