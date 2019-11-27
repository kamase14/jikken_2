import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
N = 100000

list = []

delta = 0.1
p = 0.5
U = np.random.uniform(0.0,1.0,N)
x = np.linspace(0,delta,N)
for i in U:
    if i <= delta/p:
        list.append(1)
    else:
        list.append(0)

print(np.mean(list))
print(len(x))

plt.plot(x,list)
plt.show()
