import numpy as np
import matplotlib.pyplot as plt

fx = lambda x: np.power(x,2)*np.power(np.e, x)
limite_inferior = 0
limite_superior = 3
trapecios = 4

muestras = trapecios + 1
xi = np.linspace(limite_inferior,limite_superior,muestras)
fi = fx(xi)

muestrasLineas = muestras * 10
xk = np.linspace(limite_inferior, limite_superior, muestrasLineas)
fk = fx(xk)

plt.plot(xi,fi,'ro')
plt.plot(xk,fk)

plt.fill_between(xi, 0, fi, color='y')
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color='w')

plt.show()