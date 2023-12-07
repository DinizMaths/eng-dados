from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("LetterCount").getOrCreate()

def save_postgresql(df, epoch_id):
    df.write.format("jdbc") \
        .option("url", "jdbc:postgresql://postgres:5432/banco") \
        .option("dbtable", "letter_counts") \
        .option("user", "usuario") \
        .option("password", "senha") \
        .mode("append") \
        .save()

dfEntrada = (spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "topico-letras") \
    .option("startingOffsets", "earliest") \
    .load())

dfSaida = (dfEntrada.writeStream \
    .foreachBatch(save_postgresql) \
    .outputMode("append") \
    .trigger(processingTime="5 seconds") \
    .start())

dfSaida.awaitTermination()
