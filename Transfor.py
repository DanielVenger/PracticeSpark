import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

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

# Función para calcular la transformada de Fourier y graficar el espectro
def calcular_y_graficar_transformada_de_fourier(funcion, limite_inferior, limite_superior, num_puntos):
    x = np.linspace(limite_inferior, limite_superior, num_puntos)
    y = funcion(x)
    transformada = fft(y)
    frecuencias = np.fft.fftfreq(len(transformada))
    
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    
    # Graficar la función original
    axs[0].plot(x, y)
    axs[0].set_title("Función Original")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("f(x)")
    axs[0].grid(True)
    
    # Graficar la transformada de Fourier
    axs[1].plot(frecuencias, np.abs(transformada))
    axs[1].set_title("Espectro de Fourier")
    axs[1].set_xlabel("Frecuencia")
    axs[1].set_ylabel("Amplitud")
    axs[1].grid(True)
    
    plt.tight_layout()
    plt.show()

# Menú de selección de funciones
def menu():
    print("Seleccione la función para calcular su transformada de Fourier:")
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
            calcular_y_graficar_transformada_de_fourier(f1, -4, 4, 1000)
        
        elif opcion == 2:
            calcular_y_graficar_transformada_de_fourier(f2, -4, 9, 1000)
        
        elif opcion == 3:
            calcular_y_graficar_transformada_de_fourier(f3, -10, 10, 1000)
        
        elif opcion == 4:
            calcular_y_graficar_transformada_de_fourier(f4, 0, 4, 1000)
        
        elif opcion == 5:
            calcular_y_graficar_transformada_de_fourier(f5, -5, 5, 1000)
        
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
