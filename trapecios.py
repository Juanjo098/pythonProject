"""
Programado en Python 3.10.7
Versión de numpy: 1.23.3
Versión de matplotlib: 3.6.1

Creado por:
* Guerrero Davalos Fátima Itzel
* Ochoa Vallejo Itzel
* Olivera Bautista Fátima Jhareydi
* Sánchez Figueroa Dafne
* Silva López Juan José
"""
import numpy as np
import matplotlib.pyplot as plt

valor_exacto = 98.42768

#Función para mostar la gráfica
def metodo_trapecio(trapecios, color):
    # Función
    fx = lambda x: np.power(x, 2)*np.power(np.e, x)

    limite_inferior = 0
    limite_superior = 3

    # PROCEDIMIENTO
    # Regla del Trapecio
    # Usando trapecios equidistantes en intervalo
    h = (limite_superior-limite_inferior)/trapecios
    xi = limite_inferior
    tmp = fx(xi)
    for i in range(0,trapecios-1,1):
        xi = xi + h
        tmp = tmp + 2*fx(xi)
    tmp = tmp + fx(limite_superior)
    area = h*(tmp/2)

    error = np.abs((valor_exacto - area) / valor_exacto) * 100

    # Puntos de los trapecios
    muestras = trapecios + 1
    xi = np.linspace(limite_inferior, limite_superior, muestras)
    fi = fx(xi)
    # Gráfica de la función
    muestraslinea = trapecios*10 + 1
    xk = np.linspace(limite_inferior, limite_superior, muestraslinea)
    fk = fx(xk)

    # Graficación de la función
    plt.plot(xk, fk, label='f(x)')
    plt.plot(xi, fi, marker='o', color='orange', label='muestras')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'{trapecios} trapecios\nEstimación: {area}\nValor exacto: {valor_exacto}\nError verdadero: %{error}', fontsize=8)
    plt.legend()

    # Graficación de los trapecios
    plt.fill_between(xi, 0, fi, color=color)
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color='w')

    plt.show()

#Para que muestre la siguiente gráfica, se debe cerrar ventana emergente actual.
metodo_trapecio(4, 'g')
metodo_trapecio(10, 'y')
metodo_trapecio(20, 'c')
metodo_trapecio(30, 'm')