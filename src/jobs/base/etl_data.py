import logging
import os
from abc import ABC, abstractmethod
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import SparkSession


class ETLData(ABC):
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
