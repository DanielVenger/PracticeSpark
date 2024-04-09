from pyspark import SparkContext

sc = SparkContext("local", "Ejemplo Map")

# Definir una función que multiplique un número por 2
def duplicar(numero):
    return numero * 2

# Definir una función que genere una lista de números del 0 al n-1
def llenar(n):
    lista = []
    for x in range(n):
        lista.append(x)
    return lista

# Crear un RDD a partir de la lista de números
numeros = llenar(10)
rdd = sc.parallelize(numeros)

# Aplicar la función duplicar a cada elemento del RDD utilizando map
rdd_duplicado = rdd.map(duplicar)

# Recolectar y mostrar los resultados
resultados = rdd_duplicado.collect()
print("Resultados duplicados:", resultados)
sc.stop()