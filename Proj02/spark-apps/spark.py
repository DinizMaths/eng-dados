from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

    
# Iniciar a SparkSession
spark = SparkSession.builder.appName("LetterCount").getOrCreate()

# Ler do Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "topico-letras") \
    .load() \
    .selectExpr("CAST(value AS STRING)")

# Explodir a string em letras e contar
letter_count = df \
    .select(explode(split(col("value"), "")) \
    .alias("letter")) \
    .groupBy(col("letter")) \
    .count()

# Escrever a contagem no console
query = letter_count \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .option("numRows", 10) \
    .start()
    
query.awaitTermination()
