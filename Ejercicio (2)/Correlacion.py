from pyspark import SparkContext 
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col,concat, lit
import math

def pearson(sumx,sumy,sumx2,sumy2,sumxy):
      p = ((2 * sumxy) - (sumx * sumy)) / (math.sqrt((2 * sumx2 - sumx ** 2) * (2 * sumy2 - sumy ** 2)))
      return p

def opera(x,y,archivo,r):
    filaju=archivo.filter((archivo['Item'] == x) | (archivo['Item'] == y))
    print("Se calcula el CCP de ",x ,"y",y)
    filaju.show()
    filauva=archivo.filter(archivo['Item'] == x)
    filajit=archivo.filter(archivo['Item'] == y)
    sumj= filajit.select(filajit['Dulzura'] +filajit['Crujiente']).collect()[0][0]
    sumj2=filajit.select((filajit['Dulzura'])**2+(filajit['Crujiente'])**2).collect()[0][0]
    sumu= filauva.select(filauva['Dulzura'] +filauva['Crujiente']).collect()[0][0]
    sumu2=filauva.select((filauva['Dulzura'])**2+(filauva['Crujiente'])**2).collect()[0][0]
    vjd= filauva.select('Dulzura').collect()[0][0]
    vud= filajit.select('Dulzura').collect()[0][0]
    vjc= filauva.select('Crujiente').collect()[0][0]
    vuc= filajit.select('Crujiente').collect()[0][0]
    uj=vjd*vud+vjc*vuc
    p1=pearson(sumj,sumu,sumj2,sumu2,uj)
    t=archivo.filter(archivo['Item'] == y).select('Tipo').collect()[0][0]
    print("El coeficiente de correlacion es: ", p1,"\n\n")
    r.append((t, p1))

contexto=SparkContext()
sesion=SparkSession.builder.getOrCreate()
archivo=sesion.read.option("header", "true") \
                    .option("delimiter", ",") \
                    .option("inferSchema", "true") \
                    .csv("/Users/danye/OneDrive/Escritorio/T3/Tarea.csv")

archivo.show()
r=[]
opera("Jitomate","Uva",archivo,r)
opera("Jitomate","Nuez",archivo,r)
opera("Jitomate","Haba",archivo,r)
opera("Jitomate","Naranja",archivo,r)
ro= sorted(r, key=lambda x: x[1], reverse=True)
if ro:
    tm = ro[0][0]
    vm= ro[0][1]
    print("Tipo con el mayor CPP:", tm)
    print("Valor del mayor CPP", vm)
else:
    print("No se encontraron resultados con coeficientes de correlación.")
