import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones
def f1(x):
    return np.piecewise(x, [np.logical_and(0 <= x, x < 4), np.logical_and(-4 <= x, x < 0)], [lambda x: 2*x + 4, lambda x: 4 - 2*x])

def f2(x):
    return np.piecewise(x, [np.logical_and(-4 <= x, x < 1), np.logical_and(1 <= x, x < 3), np.logical_and(3 <= x, x < 6), np.logical_and(6 <= x, x < 9)], [1, lambda x: x, lambda x: -x + 6, 0])

def f3(x):
    return np.sin(x)

def f4(x):
    return np.piecewise(x, [np.logical_and(0 <= x, x < 1), np.logical_and(1 <= x, x < 2), np.logical_and(2 <= x, x < 3), np.logical_and(3 <= x, x < 4)], [2, 0, 2, 0])

def f5(x):
    return np.exp(-x**2)

# Calcular coeficientes de la serie trigonométrica de Fourier
def calcular_coeficientes_serie_trigonométrica(funcion, limite_inferior, limite_superior, num_armonicos):
    x = np.linspace(limite_inferior, limite_superior, 1000)
    a_0 = np.mean(funcion(x))
    coeficientes_a = []
    coeficientes_b = []

    for n in range(1, num_armonicos + 1):
        coef_a = (2 / (limite_superior - limite_inferior)) * np.trapz(funcion(x) * np.cos(2 * np.pi * n * x / (limite_superior - limite_inferior)), x)
        coef_b = (2 / (limite_superior - limite_inferior)) * np.trapz(funcion(x) * np.sin(2 * np.pi * n * x / (limite_superior - limite_inferior)), x)
        coeficientes_a.append(coef_a)
        coeficientes_b.append(coef_b)

    return a_0, coeficientes_a, coeficientes_b

# Función para reconstruir la serie trigonométrica de Fourier
def reconstruir_serie_trigonométrica(x, a_0, coeficientes_a, coeficientes_b, limite_inferior, limite_superior):
    funcion_reconstruida = np.full_like(x, a_0 / 2)

    for n, (coef_a, coef_b) in enumerate(zip(coeficientes_a, coeficientes_b), start=1):
        funcion_reconstruida += coef_a * np.cos(2 * np.pi * n * x / (limite_superior - limite_inferior)) + coef_b * np.sin(2 * np.pi * n * x / (limite_superior - limite_inferior))

    return funcion_reconstruida

# Graficar la función original y la serie trigonométrica de Fourier
def graficar_funcion_y_serie_trigonométrica(funcion_original, x, funcion_reconstruida):
    plt.figure(figsize=(10, 5))
    plt.plot(x, funcion_original, label='Función original')
    plt.plot(x, funcion_reconstruida, label='Serie trigonométrica')
    plt.title('Función original y su serie trigonométrica')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Menú de selección de funciones
def menu():
    print("Seleccione la función para calcular su serie trigonométrica de Fourier:")
    print("1. f1(x)")
    print("2. f2(x)")
    print("3. f3(x)")
    print("4. f4(x)")
    print("5. f5(x)")
    print("0. Salir")

# Función principal
def main():
    while True:
        menu()
        opcion = int(input("Ingrese el número de la función (0 para salir): "))
        
        if opcion == 0:
            print("¡Hasta luego!")
            break
        
        elif opcion == 1:
            a_0, coeficientes_a, coeficientes_b = calcular_coeficientes_serie_trigonométrica(f1, -4, 4, 10)
            x = np.linspace(-4, 4, 1000)
            funcion_reconstruida = reconstruir_serie_trigonométrica(x, a_0, coeficientes_a, coeficientes_b, -4, 4)
            graficar_funcion_y_serie_trigonométrica(f1(x), x, funcion_reconstruida)
        
        elif opcion == 2:
            a_0, coeficientes_a, coeficientes_b = calcular_coeficientes_serie_trigonométrica(f2, -4, 9, 10)
            x = np.linspace(-4, 9, 1000)
            funcion_reconstruida = reconstruir_serie_trigonométrica(x, a_0, coeficientes_a, coeficientes_b, -4, 9)
            graficar_funcion_y_serie_trigonométrica(f2(x), x, funcion_reconstruida)
        
        elif opcion == 3:
            a_0, coeficientes_a, coeficientes_b = calcular_coeficientes_serie_trigonométrica(f3, -10, 10, 10)
            x = np.linspace(-10, 10, 1000)
            funcion_reconstruida = reconstruir_serie_trigonométrica(x, a_0, coeficientes_a, coeficientes_b, -10, 10)
            graficar_funcion_y_serie_trigonométrica(f3(x), x, funcion_reconstruida)
        
        elif opcion == 4:
            a_0, coeficientes_a, coeficientes_b = calcular_coeficientes_serie_trigonométrica(f4, 0, 4, 10)
            x = np.linspace(0, 4, 1000)
            funcion_reconstruida = reconstruir_serie_trigonométrica(x, a_0, coeficientes_a, coeficientes_b, 0, 4)
            graficar_funcion_y_serie_trigonométrica(f4(x), x, funcion_reconstruida)
        
        elif opcion == 5:
            a_0, coeficientes_a, coeficientes_b = calcular_coeficientes_serie_trigonométrica(f5, -5, 5, 10)
            x = np.linspace(-5, 5, 1000)
            funcion_reconstruida = reconstruir_serie_trigonométrica(x,a_0,coeficientes_a, coeficientes_b, -5, 5)
            graficar_funcion_y_serie_trigonométrica(f5(x),x,funcion_reconstruida)

if __name__ == "__main__":
    main()