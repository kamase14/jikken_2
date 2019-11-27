import numpy as np
import matplotlib.pyplot as plt

np.random.seed()
N = 100000
U = np.random.uniform(0.0,1.0,N)
ramda = 1

X = -1/ramda * np.log(1-U)
X.sort()
print(X)

y,binEdges=np.histogram(data,bins=100)
bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
p.plot(bincenters,y,'-')
plt.grid(True)
plt.show()
