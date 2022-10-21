"""
Creado por:
* Guerrero Davalos Fátima Itzel
* Ochoa Vallejo Itzel
* Olivera Bautista Fátima Jhareydi
* Sánchez Figueroa Dafne
* Silva López Juan José

Programado en Python 3.10.7
Versión de numpy: 1.23.3
Versión de pandas: 1.5.1
Versión de matplotlib: 3.6.1
Versión de statsmodels: 0.13.2
"""

# Importar las librerias que se va a utilizar
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

# Listas que contienen los datos a graficar
X= [[0,0],[0,2],[1,2],[2,4],[0,4],[1,6],[2,6],[2,2],[1,1]]
Y= [14, 21, 11, 12, 23, 23, 14, 6 ,11]

# Definir la entrada para pandas
df2=pd.DataFrame(X,columns=['x0','x1'])
df2['y']=pd.Series(Y)
df2

# Aplicaciar la regresión lineal múltiple
model = smf.ols(formula='y ~ x0 + x1', data=df2)
results_formula = model.fit()
results_formula.params

# Adaptar los datos para graficarlos
x_surf, y_surf = np.meshgrid(np.linspace(df2.x0.min(), df2.x0.max(), 100),np.linspace(df2.x1.min(), df2.x1.max(), 100))
onlyX = pd.DataFrame({'x0': x_surf.ravel(), 'x1': y_surf.ravel()})
fittedY=results_formula.predict(exog=onlyX)

# Convertir los resultados en un array para su posterior graficación
fittedY=np.array(fittedY)

# Graficar los datos originales y el modelo de regresión lineal múltiple
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df2['x0'],df2['x1'],df2['y'],c='red', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='b', alpha=0.3)
ax.set_xlabel('x0')
ax.set_ylabel('x1')
ax.set_zlabel('y')
plt.title('Regresión lineal múltile')
plt.show()