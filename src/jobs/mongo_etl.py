from jobs.etl import Etl
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession
from common.utils import check_data_quality
import great_expectations as ge

class MongoETL(Etl):        
    def __init__(self, spark: SparkSession, database, collection, ge_file_name: str):
        super().__init__(spark)        
        self.database = database
        self.collection = collection
        self.client = None
        self.db = None
        self.ge_file_name = ge_file_name
    
    def extract(self) -> DataFrame:
        print(self.database)
        print(self.collection)
        df = self.spark.read.format("mongodb") \
            .option("database",self.database) \
            .option("collection",self.collection) \
            .load()
        df.printSchema()        
        return df
    
    def validate(self, df: DataFrame) -> None:
        check_data_quality(self.ge_file_name,df,f'mongodb_{self.database}_{self.collection}')
    
    def transform(self, df: DataFrame) -> DataFrame:
        df_cleaned = df
        return df_cleaned
    
    def load(self, df: DataFrame):
        df.write \
            .format("parquet") \
            .mode("overwrite") \
            .save(f"s3a://dp-source/{self.database}/{self.collection}")
        