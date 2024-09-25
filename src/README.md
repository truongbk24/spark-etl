# Spark Ingestion project

This project aim to extract the data from datasources and load to Minio Storage

## Structure of the project

We splitted the project into different layer as below

- common: In this folder, there're some common to supporting the job such as: get data from vault, send_email, check data quality....
- config: the json file will have the configuration for great_expectations data quality for each table
- job: Contains multiple pyspark code.
    Based on the factory pattern, we designed to implement multiple source for spark job:
        + etl.py: The base class in which different source need to inherit then implement the own method
        + jdbc_etl.py: Inherit from base class etl, init the spark session to read from database table, then write to Minio storage
        + mongo_etl.py: Inherit from base class etl, init the spark session to read from mongodb collection, then write to Minio storage
        + factory_etl.py: The factory class to direct which class should be implemented
        + main.py: The main class to run the spark jobs


## How to run the spark job

Prerequisite: The vault secret for each type. Take a look at file script.sh at folder container\vault.

Submit the Spark job within spark-submit command, 3 parameters need to be provided:
- source_type: The source type of the source table, for example: mongodb, jdbc_mysql, jdbc_oracle,...
- source_name: The database name associated within the source_type
- source_table: The table you want to extract and load

spark-submit --packages src/main.py --source_type "mongodb" --source_name "crm" --table_name "customer"

