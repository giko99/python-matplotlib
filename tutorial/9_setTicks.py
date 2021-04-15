import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(0,360,1)
y = np.sin(np.deg2rad(sudut))

# buat plot
plt.plot(sudut,y)
plt.ylabel("magnitudo")
plt.xlabel("sudut")

plt.yticks([-1,0,1])
plt.xticks(
    [0         ,90         ,180         ,270         ,360],
    [r'${0}^0$',r'${90}^0$',r'${180}^0$',r'${270}^0$',r'${360}^0$'])

# tampilkan plot
plt.show()