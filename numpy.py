import numpy as np
import matplotlib.pyplot as plt
myPoly = np.polydl(np.array([3,-1,1]))
astype(float)
x = np.linspace(-5,5,100)
y = myPoly(x)
plt.xlabel('x values')
plt.ylabel('f(x) values')
xticks = np.arange(-5, 5,10)
yticks = np,arange(0,100,10)
plt.xticks(xticks)
plt.yticks(yticks)
plt.grip(True)
plt.plot(x,y)