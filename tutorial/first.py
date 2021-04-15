import numpy as np
import matplotlib.pyplot as plt

a=[1,2,3,4,5]
b=[1,2,3,4,5]

PI = np.pi
sudut = np.linspace(0,2*PI,100)
radius = 5;
x=radius* np.cos(sudut)
y=radius* np.sin(sudut)

#inisiasi plot
plt.plot(x,y)

#tampilkan
plt.show()