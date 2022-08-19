import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.title("Graph")
plt.xlabel('Nischal')
plt.ylabel('kafle')
plt.grid()
plt.axhline(0.25)
plt.axvline(0.25)
plt.axhline(linewidth=1)
a=[1,2,3,4,5,7,8]
b=[2,5,6,7,8,2,1,9,0]
plt.scatter(x,y,marker='+')
plt.show()

