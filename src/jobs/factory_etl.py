from jobs.jdbc_etl import JdbcETL
from jobs.etl import Etl
from jobs.mongo_etl import MongoETL
from pyspark.sql import SparkSession

class EtlFactory:    
    @staticmethod
    def get_etl(etl_type: str, spark: SparkSession, **kwargs) -> Etl:
        if 'jdbc' in etl_type:
            return JdbcETL(spark, kwargs['jdbc_url'], kwargs['database'] ,kwargs['jdbc_properties'], kwargs['table_name'], kwargs['ge_file_name'])
        elif etl_type == 'mongodb':
            return MongoETL(spark, kwargs['database'], kwargs['collection'], kwargs['ge_file_name'])
        else:
            raise ValueError(f"Unknown ETL type: {etl_type}")