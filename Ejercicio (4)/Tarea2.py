from pyspark import SparkContext 
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col
import math
import tkinter as tk
from tkinter import filedialog
import sys
from io import StringIO

def spark(ruta):
    contexto=SparkContext()
    sesion=SparkSession.builder.getOrCreate()
    archivo=sesion.read.option("header", "true") \
                        .option("delimiter", ",") \
                        .option("inferSchema", "true") \
                        .csv(ruta)
    #Se creo la columna XY 
    archivo = archivo.withColumn("XY", col("X") * col("Y"))
    #Se creo la columna X2 
    archivo = archivo.withColumn("X2", col("X") * col("X"))
    #Se creo la columna Y2 
    archivo = archivo.withColumn("Y2", col("Y") * col("Y"))
    #Suma de cada columna
    sumx=archivo.select(sum(archivo.X)).collect()[0][0]
    sumy=archivo.select(sum(archivo.Y)).collect()[0][0]
    sumxy=archivo.select(sum(archivo.XY)).collect()[0][0]
    sumx2=archivo.select(sum(archivo.X2)).collect()[0][0]
    sumy2=archivo.select(sum(archivo.Y2)).collect()[0][0]

    #Estas lineas tienen el proposito de guardar el contenido de show() como texto 
    sal=sys.stdout
    sys.stdout=StringIO()
    archivo.show()
    matriz=sys.stdout.getvalue()
    sys.stdout=sal

    #Se muestra la tabla final en la interfaz
    texto_resultados.insert(tk.END, "Matriz de Datos:\n")
    texto_resultados.insert(tk.END, matriz)
    texto_resultados.insert(tk.END, "\n")
    texto_resultados.insert(tk.END, "Resultados:\n")
    texto_resultados.insert(tk.END, f"La suma de X: {sumx}\n")
    texto_resultados.insert(tk.END, f"La suma de Y: {sumy}\n")
    texto_resultados.insert(tk.END, f"La suma de XY: {sumxy}\n")
    texto_resultados.insert(tk.END, f"La suma de X2: {sumx2}\n")
    texto_resultados.insert(tk.END, f"La suma de Y2: {sumy2}\n")
    n = archivo.count()
    p = ((n * sumxy) - (sumx * sumy)) / (math.sqrt((n * sumx2 - sumx ** 2) * (n * sumy2 - sumy ** 2)))
    texto_resultados.insert(tk.END, f"El coeficiente de correlación de Pearson es: {p}\n")


def abrir_explorador():
    csv=filedialog.askopenfilename(filetypes=[("Archivo CSV","*.csv")])
    if csv:
        entrada_archivo.delete(0,tk.END)
        entrada_archivo.insert(0,csv)
        spark(csv)

ventana=tk.Tk()
ventana.title("Pearson-BigData")
entrada_archivo=tk.Entry(ventana, width=50)
entrada_archivo.pack(pady=10)
boton=tk.Button(ventana, text="Seleccionar Archivo", command=abrir_explorador)
boton.pack(pady=5)
texto_resultados=tk.Text(ventana, width=80, height=20)
texto_resultados.pack(pady=10)

ventana.mainloop()
