import matplotlib.pyplot as plt
import math
import numpy as np

def f1(x):
    return 1/(1+np.exp(-x))

def f2(x):
    return (2/(1+np.exp(-2*x)))-1

def f3(x):
    y3 = []
    for i in range(len(x)):
        if x[i]>=0:
            y3.append(1)
        else:
            y3.append(0)
    return y3

x = np.linspace(-10,10,1000)

y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

print(x.shape)
print(y1)
print(y2)
print(y3)

plt.figure(figsize=(15,4))
plt.subplot(1,3,1,polar=False)
plt.plot(x,y1,color="blue",linewidth=2)
plt.grid(linestyle='-.')
plt.subplot(1,3,2,polar=False)
plt.plot(x,y2,color="blue",linewidth=2)
plt.grid(linestyle='-.')
plt.subplot(1,3,3,polar=False)
plt.plot(x,y3,color="blue",linewidth=2)
plt.grid(linestyle='-.')
plt.savefig("1.svg")
plt.show()



