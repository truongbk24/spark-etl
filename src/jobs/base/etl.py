from abc import ABC, abstractmethod
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession


class Etl(ABC):
    def __init__(self, spark: SparkSession):
        self.spark = spark
    
    @abstractmethod    
    def extract(self) -> DataFrame:
        pass
    
    @abstractmethod
    def transform(self, df: DataFrame) -> DataFrame:
        pass
    
    @abstractmethod
    def load(self, df: DataFrame) -> None:
        pass
    
    def run(self):
        df = self.extract()
        df_transformed = self.transform(df)
        self.load(df_transformed)
