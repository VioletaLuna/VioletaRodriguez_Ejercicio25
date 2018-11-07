#Este archivo usa ecoding: utf-8
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("sample.dat", delimiter = " ", skip_header = 0)
muestra = data
print(muestra.size)


plt.hist(muestra )

plt.show()
#plt.savefig("grafica.png")
