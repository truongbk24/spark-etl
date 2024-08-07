import logging
from pyspark.sql import SparkSession
from jobs.base.factory_etl import EtlFactory
from common.constant import RDBMS_URL, RDBMS_CONNECTION_PROPERTIES

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("ETL Factory Example") \
        .getOrCreate()
        

    etl_type = 'jdbc'  # or 'jdbc'
    
    if etl_type == 'csv':
        etl = EtlFactory.get_etl(etl_type, spark, source_path="path/to/source_data.csv")
    elif etl_type == 'jdbc':
        jdbc_url = RDBMS_URL
        jdbc_properties = RDBMS_CONNECTION_PROPERTIES
        print(RDBMS_CONNECTION_PROPERTIES)
        etl = EtlFactory.get_etl(etl_type, spark, jdbc_url=jdbc_url, jdbc_properties=jdbc_properties, table_name="Categories")

    etl.run()