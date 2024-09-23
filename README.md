# Data Engineering Project
This project was done for demostration loading data through a couple of layers and visualize in dashboard for end-users can view the final data.

## Overview of the Architecture

![overview](./asset/images/data_engineering_batch.drawio.png)

Assume that we need to ingest data from multiple source into data platform, process the data. Here are the tech stack for this demo:

1. **`Apache Spark`**: Extract and load the data from sources to data storage
2. **`Great Expectations`**: Framework integrate with Apache Spark for checking data quality for datafrom loading from sources
3. **`HashiCorp Vault`**: Save the secrets by key, value such as: host, port, username, password
4. **`Minio`**: Data store to store the data as file
5. **`Dbt (Data Build Tool)`**: The transformation tool for processing data
6. **`Apache Airflow`**: Schedule and orchestra the DAGs
7. **`Apache Superset`**: The visualization tools for reporting and dashboard
8. **`Clickhouse`**: The data analytics platform for handling huge data extremely fast

## Structure of the folder
![structure](./asset/images/folder_structure.png)

### Structure of folder container

This folder contains everything we need to setup the infrastucture

#### Structure of folder airflow

![airflow](./asset/images/airflow_folder.png)

#### Structure of folder mongodb
![mongodb](./asset/images/mongodb_folder.png)

#### Structure of folder mysql
![mysql](./asset/images/mysql_folder.png)

#### Structure of folder spark
![spark](./asset/images/spark_folder.png)

#### Structure of folder superset
![superset](./asset/images/superset_folder.png)

#### Structure of folder vault
![vault](./asset/images/vault_folder.png)