import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir símbolos
x, n = sp.symbols('x n')

def introducir_funcion():
    # Permitir al usuario introducir su propia función.
    func_input = input('Ingresa la función f(x): ')
    f = sp.sympify(func_input)
    return f

def calcular_coeficientes(f, L, N):
    # Calcula coeficientes a0, an, bn
    a0 = (1/L) * sp.integrate(f, (x, -L, L))
    aN = [(1/L) * sp.integrate(f * sp.cos((n * sp.pi * x) / L), (x, -L, L)).simplify() for n in range(1, N+1)]
    bN = [(1/L) * sp.integrate(f * sp.sin((n * sp.pi * x) / L), (x, -L, L)).simplify() for n in range(1, N+1)]
    return a0, aN, bN

def calcular_serie(x_vals, a0, aN, bN, L, N):
    # Calcula la serie de Fourier
    f_series = a0 / 2
    for n in range(1, N+1):
        f_series += aN[n-1] * sp.cos((n * sp.pi * x) / L) + bN[n-1] * sp.sin((n * sp.pi * x) / L)
    f_series = sp.lambdify(x, f_series, 'numpy')
    y_vals = f_series(x_vals)
    return y_vals

def mostrar_resultado(a0, aN, bN):
    # Mostrar los coeficientes de forma general.
    print("Coeficientes de la Serie de Fourier:")
    print("a0 =", a0)
    for i, (aN_val, bN_val) in enumerate(zip(aN, bN)):
        print("a{} = {}".format(i+1, aN_val))
        print("b{} = {}".format(i+1, bN_val))

def main():
    print("Este programa calcula los coeficientes de la Serie de Fourier para una función dada.")
    f = introducir_funcion()
    L = float(input('Ingresa el medio periodo L (donde el periodo total es 2L): '))
    N = int(input('Ingresa el número de términos a considerar en la serie de Fourier: '))
    
    # Calcular coeficientes
    a0, aN, bN = calcular_coeficientes(f, L, N)
    mostrar_resultado(a0, aN, bN)
    
    # Definir el rango para la gráfica
    x_vals = np.linspace(-L, L, 100)
    
    # Calcular la serie de Fourier
    y_vals_serie = calcular_serie(x_vals, a0, aN, bN, L, N)
    
    # Convertir la función original a una función numpy
    f_np = sp.lambdify(x, f, 'numpy')
    y_vals_original = f_np(x_vals)
    
    # Graficar la serie de Fourier y la función original1
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals_original, label='Función Original', color='blue')
    plt.plot(x_vals, y_vals_serie, label='Serie de Fourier', linestyle='--', color='red')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Función Original vs. Serie de Fourier')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
