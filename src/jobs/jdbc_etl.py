from jobs.etl import Etl
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession
from common.utils import check_data_quality
import great_expectations as ge
from great_expectations.core.batch import BatchRequest
from great_expectations.execution_engine.sparkdf_execution_engine import SparkDFExecutionEngine

class JdbcETL(Etl):        
    def __init__(self, spark: SparkSession, jdbc_url: str, database: str, jdbc_properties: dict, table_name: str, ge_file_name: str):
        super().__init__(spark)
        self.jdbc_url = jdbc_url
        self.database=database
        self.jdbc_properties = jdbc_properties
        self.table_name = table_name
        self.ge_file_name = ge_file_name
    
    def extract(self) -> DataFrame:
        query = f"(SELECT * FROM {self.table_name}) as temp"
        df = self.spark.read.jdbc(url=self.jdbc_url, table=query, properties=self.jdbc_properties)
        return df
    
    def validate(self, df: DataFrame) -> None:
        check_data_quality(self.ge_file_name,df,f'jdbc_{self.database}_{self.table_name}')
        
    
    def transform(self, df: DataFrame) -> DataFrame:
        df_cleaned = df
        return df_cleaned
    
    def load(self, df: DataFrame):
        df.write \
            .format("parquet") \
            .mode("overwrite") \
            .save(f"s3a://dp-source/{self.database}/{self.table_name}/")