spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 spark_stream.py
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 --master spark://localhost:7077 spark_stream.py

docker exec -it cassandra cqlsh -u cassandra -p cassandra localhost 9042
select * from spark_streams.created_users;