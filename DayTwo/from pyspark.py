from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
# Crear la sesión de Spark
spark = SparkSession.builder.getOrCreate()

dir = "/Users/danye/OneDrive/Escritorio/prueba.csv"

# Leer el archivo CSV
sparkArchivo = spark.read.option("header", "true")\
    .option("delimiter", ",") \
    .option("inferSchema", "true") \
    .csv(dir)
sparkArchivo.show()
Columnas=sparkArchivo.select("ATRIBUTO_2","ATRIBUTO_4")
Columnas.show()

Renglones=sparkArchivo.filter(sparkArchivo.Atributo_1<40)
Renglones.show()

Renglones2=sparkArchivo.filter(sparkArchivo.Atributo_2<40)
Renglones2.show()

Columna=Renglones2.select("Atributo_1")
Columna.show()

print(Columna.collect()[1])

subconjunto=sparkArchivo.drop("Atributo_3")
subconjunto2=subconjunto.withColumn("NuevaPrueba",subconjunto["Atributo_5"]+2)
subconjunto2.show()

subconjunto2.select(sum(subconjunto2.Atributo_1)+2).show()