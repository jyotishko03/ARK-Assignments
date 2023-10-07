import numpy as np
import matplotlib.pyplot as plt

a=np.random.normal(loc=0.5, scale=2.0, size=100000)
b=np.random.uniform(low=0, high=10, size=100000)


#c
a_mean=np.mean(a)
a_std=np.std(a)
print(f"a_mean={a_mean}, a_std={a_std}")

b_mean=np.mean(b)
b_std=np.std(b)
print(f"b_mean={b_mean}, b_std={b_std}")

#Yes, for a, we have defined the mean and stndard distribution
#for b, its uniform so its easily understandible and calculatible

#d
plt.hist(a, bins=500)
plt.show()

plt.hist(b, bins=500)
plt.show()

'''
e
For same distribution everytime,
fixed=np.randomrandom.RandomState(23479) , a seed inside bracket
a=fixed.normal(loc=0.5, scale=2.0, size=100000)
b=fixed.uniform(low=0, high=10, size=100000)
above changes made from line 4
'''