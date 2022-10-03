"""
Programado en Python 3.7.10
Versión de numpy: 1.23.3

Creado por:
* Guerrero Davalos Fátima Itzel
* Ochoa Vallejo Itzel
* Olivera Bautista Fátima Jhareydi
* Sánchez Figueroa Dafne
* Silva López Juan José
"""
import numpy as np

array = np.array([[3, 4, -10], [9, 2, -1], [7, 8, 5]], dtype="float32")
results = np.array([-2, 3, 6], dtype="float32")
#array = 0
#results = 0
iteration_limit = 0
tolerance_percentage = 0.0

def input_int(promt):
    # Permite ingresar un valor de tipo entero

    # Parámetros:
    #   promt: Mensaje a mostrar

    # Retorno:
    #   Valor de tipo entero

    try:
        return int(input(promt))
    except ValueError:
        print("ERROR. Ingrese un valor numérico.\n")
        return input_int(promt)

def input_float(promt):
    # Permite ingresar un valor de tipo flotante

    # Parámetros:
    #   promt: Mensaje a mostrar

    # Retorno:
    #   Valor de tipo flotante

    try:
        return float(input(promt))
    except ValueError:
        print("ERROR. Ingrese un valor numérico.\n")
        return input_float(promt)

def define_matrix():
    global array
    global results
    global iteration_limit
    global tolerance_percentage
    size = 0
    while True:
        size = input_int("Ingresa el tamaño de la matriz: ")
        if size > 1: break
        else: print("El tamaño de la matriz no puede ser menor a 0\n")

    while True:
        iteration_limit = input_int("Ingresa el número máximo de iteraciones: ")
        if iteration_limit > 0: break
        else: print("El límite de iteraciones debe ser mayor a 0\n")

    while True:
        tolerance_percentage = input_float("Ingresa el margen de tolerancia: ")
        if tolerance_percentage > 0: break
        else: print("El margen de tolerancia debe ser mayor a 0\n")

    tmp_array = []
    tmp_res = []

    for row in range(size):
        tmp = []
        for column in range(size):
            tmp.append(input_float(f"Ecuación {row+1}, x{column + 1}: "))
        tmp_array.append(tmp)
        tmp_res.append(input_float(f"Resultado de la ecuación {row + 1}: "))

    array = np.array(tmp_array, dtype="float64")
    results = np.array(tmp_res, dtype="float64")

def sort_array():
    global array
    global results
    v = []
    for a in range(len(array)):
        v.append(np.argmax(np.absolute(array[a])))
    #print(v)
    for i in range(len(v)):
        if i == len(v)-1:
            break
        else:
         if v[i] == v[i+1]:
            print("Ey eso no se vale")
            return False
    ordenada = []
    resord = []
    #print()
    for o in range(len(v)):
        ordenada.insert(o,array[v.index(o)])
        resord.insert(o,results[v.index(o)])
        #print(ordenada[o]," --> ",resord[o])
    array = np.array(ordenada, dtype="float32")
    results = np.array(resord, dtype="float32")
    return True

def process(array, results, iteration_limit: int, tolerance_percentage: float):
    """
    Calcula los valores de las incognitas de un sistema de ecuaciones de n x n con el método de Gauss-Seidel
    :param array: Array que contiene los coeficientes del sistema de ecuaciones
    :param results: Array que contiene los resultados de ecuaciones
    :param iteration_limit: Número máximo de iteraciones que se realizarán en caso de no alcanzar el porcentaje de tolerancia de error
    :param tolerance_percentage: Porcentaje de tolerancia de error
    :return: Numpy array que contiene los valores de las incognitas
    """
    xs = np.zeros(len(array)).astype("float32")
    errors = np.zeros(len(array)).astype("float32")

    iteration = 0

    while True:

        ant = np.copy(xs)

        #Ciclo para alcular los valores de x
        for row in range(len(array)):
            result = 0
            for column in range(len(array)):
                if column != row:
                    result -= array[row][column] * xs[column]
            xs[row] = (result + results[row]) / array[row][row]

        #Ciclo para calcular el error aproximado
        for e in range(len(xs)):
            errors[e] = abs(((xs[row] - ant[row]) / xs[row]) * 100.0)

        iteration += 1

        #Determina si el mayor error aproximado de las icognitas esta por debajo del procentaje de tolerancia de error
        if np.amax(np.absolute(errors)) < tolerance_percentage:
            print(f"Se alcanzó el porcentaje de tolerancia en la iteración: {iteration}")
            show_array(array,results)
            show_results(xs)
            return xs

        # Determina si se alcanzó el límite de iteraciones
        if iteration == iteration_limit:
            print("Se alcanzó el límite de iteraciones")
            show_array(array, results)
            show_results(xs)
            return xs

def print_1d_array(array):
    for a in array:
        print(a, end=", ")

def show_2d_array(array):
    for row in range(len(array)):
        for column in range(len(array[row])):
            print(f"{array[row][column]} \t", end="")
        print(results[row])

def show_results(xs):
    for r in range(len(xs)):
        print(f"x{r+1}: {xs[r]}")

def show_array(array, resulst):
    for row in range(len(array)):
        for column in range(len(array[row])):
                print((f"+{array[row][column]}" if array[row][column] > 0 else f"+{array[row][column]}"), end="")
        print(f"={results[row]}")

define_matrix()
if sort_array():
    process(array, results, iteration_limit, tolerance_percentage)