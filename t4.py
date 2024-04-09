from pyspark import SparkContext 
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col
from tkinter import filedialog
import math

ruta=filedialog.askopenfilename(filetypes=[("Archivo CSV", "*.csv")])      
contexto=SparkContext()
sesion=SparkSession.builder.getOrCreate()
archivo=sesion.read.option("header", "true") \
                    .option("delimiter", ",") \
                    .option("inferSchema", "true") \
                    .csv(ruta)


def linear(sumxy,n,sumx,sumy,sumx2):
    promx=sumx/n
    promy=sumy/n
    k=sumxy-n*promx*promy
    w=sumx2-n*(promx**2)
    m=k/w
    b=promy-m*promx
    return m,b
def newvalue(m,b,v):
    valor=m*v+b
    return valor
def vac(df):
    return df.na.drop()
archivo=vac(archivo)
name1=archivo.columns[0]
name2=archivo.columns[1]
name3=archivo.columns[2]

def corre(X, Y, archivo):
    archivo = archivo.withColumn("XY", col(X) * col(Y))
    archivo = archivo.withColumn("X2", col(X) * col(X))
    archivo = archivo.withColumn("Y2", col(Y) * col(Y))
    sumx = archivo.select(sum(col(X))).collect()[0][0]  
    sumy = archivo.select(sum(col(Y))).collect()[0][0] 
    sumxy = archivo.select(sum(archivo.XY)).collect()[0][0]
    sumx2 = archivo.select(sum(archivo.X2)).collect()[0][0]
    sumy2 = archivo.select(sum(archivo.Y2)).collect()[0][0]
    n = archivo.count()
    p = ((n * sumxy) - (sumx * sumy)) / (math.sqrt((n * sumx2 - sumx ** 2) * (n * sumy2 - sumy ** 2)))
    print("El coeficiente de correlación de Pearson en",Y,":", p, "\n")
    return p


def ecm(X,Y,archivo):
    n = archivo.count()
    multi=archivo.withColumn("XY", col(X) * col(Y))
    x2=archivo.withColumn("X2", col(X) * col(X))
    sumxy=multi.select(sum(multi.XY)).collect()[0][0]
    sumx2=x2.select(sum(x2.X2)).collect()[0][0]
    sumx = archivo.select(sum(col(X))).collect()[0][0] 
    sumy = archivo.select(sum(col(Y))).collect()[0][0]
    q=linear(sumxy,n,sumx,sumy,sumx2)
    print("\n\nLa ecuación de la recta de mejor ajuste de",Y,"es:\n y={:.4f}x+{:.4f}\n".format(q[0], q[1]))
    archivo=archivo.withColumn("YR",col(X)*q[0]+q[1])
    archivo=archivo.withColumn("YR2",(col(Y)-col("YR"))**2)
    ecm=math.sqrt(archivo.select(sum(archivo.YR2)).collect()[0][0]/n)
    print("Podemos calcular el valor estimado de su propiedad\n")
    v = None
    while v is None:
        try:
            v = float(input("Ingrese el tamaño de su propiedad: "))
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    t=newvalue(q[0],q[1],v)
    print("El costo estimado de su propiedad es de:${:.2f} MXN\n".format(t))
    print("Tomando en cuenta el error cuadratico medio=$(",t-ecm,t,t+ecm,")\n\n\n\n")

h1=corre(name1,name2, archivo)
h2=corre(name1,name3,archivo)

if(h1>h2):
    print("La variable con mejor relacion es ",name2,"\n")
    ecm(name1,name2,archivo)
else:
    print("La variable con mejor relacion es ",name3,"\n")
    ecm(name1,name3,archivo)



