from pyspark import SparkContext 
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import math

contexto = SparkContext()
sesion = SparkSession.builder.getOrCreate()
direccion = "/Users/danye/OneDrive/Escritorio/Ejercicio/1.csv"

def opera(dataframe):
    x = dataframe.collect()[0][1] - dataframe.collect()[1][1]
    y = dataframe.collect()[0][2] - dataframe.collect()[1][2]
    x2 = x * x
    y2 = y * y
    suma_cuadrados = x2 + y2
    distancia = math.sqrt(suma_cuadrados)
    return distancia

archivo = sesion.read.option("header", "true") \
                     .option("delimiter", ",") \
                     .option("inferSchema", "true") \
                     .csv(direccion)

columna = archivo.select("IDENTIFICADOR")
archivo.show()

distancias = []
num_filas = columna.count()

for i in range(num_filas - 1):
    subconjunto = archivo.filter((col("Identificador") == archivo.collect()[i][0]) | (col("Identificador") == num_filas))
    subconjunto = subconjunto.drop("PESO")
    subconjunto.show()
    distancias.append((opera(subconjunto), i))

print(distancias)
distancia_minima = min(distancias)
print(distancia_minima)
print("El estimado es:", archivo.collect()[distancia_minima[1]][2])
