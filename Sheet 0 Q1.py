import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)*np.cos(x)
#math is not used as it wil be used by multiple values



x = np.linspace(-2*np.pi, 2*np.pi, 1000)

plt.plot(x, f(x))
#plt.savefig('sheet1 Q2 plot.png')
plt.show()