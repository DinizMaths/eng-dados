docker exec -it postgres bash
psql -d banco -U usuario -W
senha

CREATE TABLE letter_counts (
    letter CHAR(1),
    count BIGINT
);

SELECT * FROM letter_counts;


docker exec -it kafka bash
kafka-topics.sh --create --topic topico-letras --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1
kafka-topics.sh --list --bootstrap-server kafka:9092
kafka-console-producer.sh --topic topico-letras --bootstrap-server kafka:9092


docker exec -it spark-master /bin/bash
cd /opt/spark/
./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 ./spark-apps/spark.py


./bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 --jars ./jars/postgresql-42.2.23.jar ./spark-apps/spark-postgres.py

kafka-console-consumer.sh --topic topico-letras --from-beginning --bootstrap-server kafka:9092
