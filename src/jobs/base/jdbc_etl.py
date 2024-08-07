from jobs.base.etl import Etl
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession

class JdbcETL(Etl):        
    def __init__(self, spark: SparkSession, jdbc_url: str, jdbc_properties: dict, table_name: str):
        super().__init__(spark)
        self.jdbc_url = jdbc_url
        self.jdbc_properties = jdbc_properties
        self.table_name = table_name
    
    def extract(self) -> DataFrame:
        query = f"(SELECT * FROM {self.table_name}) as temp"
        df = self.spark.read.jdbc(url=self.jdbc_url, table=query, properties=self.jdbc_properties)
        return df
    
    def transform(self, df: DataFrame) -> DataFrame:
        df_cleaned = df
        return df_cleaned
    
    def load(self, df: DataFrame):
        df.show(10)