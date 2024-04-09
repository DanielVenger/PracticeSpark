from pyspark import SparkContext 
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col,concat, lit
import math

def dist(x1,x2,y1,y2):
      d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
      return d
def opera(x,y,archivo,r):
    filaju=archivo.filter((archivo['Item'] == x) | (archivo['Item'] == y))
    print("Se calcula la distancia entre ",x ,"y",y)
    filaju.show()
    x2=filaju.filter(filaju.Item ==x).select("Dulzura").collect()[0][0]
    x1=filaju.filter(filaju.Item==y).select("Dulzura").collect()[0][0]
    y2=filaju.filter(filaju.Item==x).select("Crujiente").collect()[0][0]
    y1=filaju.filter(filaju.Item==y).select("Crujiente").collect()[0][0]
    d=dist(x1,x2,y1,y2)
    print("La distancia entre los dos puntos es: ", d,"\n")
    t=archivo.filter(archivo['Item'] == y).select('Item').collect()[0][0]
    r.append((t, d))

contexto=SparkContext()
sesion=SparkSession.builder.getOrCreate()
archivo=sesion.read.option("header", "true") \
                    .option("delimiter", ",") \
                    .option("inferSchema", "true") \
                    .csv("/Users/danye/OneDrive/Escritorio/KNN/Tarea.csv")

archivo.show()
r=[]
opera("Jitomate","Uva",archivo,r)
opera("Jitomate","Nuez",archivo,r)
opera("Jitomate","Haba",archivo,r)
opera("Jitomate","Naranja",archivo,r)

resultados_ordenados = sorted(r, key=lambda x: x[1], reverse=False)

if resultados_ordenados:
    mt = resultados_ordenados[0][0]
    mv= resultados_ordenados[0][1]
    print("El elemento con menor distancia es: ", mt)
    print("Valor de la distancia", mv)
else:
    print("No se encontraron distancias")
