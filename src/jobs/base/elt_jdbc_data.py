from etl_data import ETLData
from common.jdbc_connection import SparkJDBCConnection
from pyspark.sql.dataframe import DataFrame
from common.util import RDBMS_CONNECTION_PROPERTIES

class ETLJDBCData(ETLData):
    def extract(self) -> DataFrame:
        jdbc_conn = SparkJDBCConnection(**RDBMS_CONNECTION_PROPERTIES)
        df = jdbc_conn.read_table('test')
        return df
        