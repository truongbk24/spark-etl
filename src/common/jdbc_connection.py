from pyspark.sql import SparkSession

class SparkJDBCConnection:
    def __init__(self, jdbc_url, jdbc_driver, jdbc_user, jdbc_password, spark):
        self.jdbc_url = jdbc_url
        self.jdbc_driver = jdbc_driver
        self.jdbc_user = jdbc_user
        self.jdbc_password = jdbc_password
        self.spark = self._create_spark_session

    def _create_spark_session(self):
        spark = SparkSession.builder \
            .appName("Spark JDBC Connection") \
            .config("spark.jars.packages", self.jdbc_driver) \
            .getOrCreate()
        return spark
    
    def read_table(self, table_name):
        try:
            df = self.spark.read \
                .format("jdbc") \
                .option("url", self.jdbc_url) \
                .option("dbtable", table_name) \
                .option("user", self.jdbc_user) \
                .option("password", self.jdbc_password) \
                .option("driver", self.jdbc_driver) \
                .load()
            print(f"Data from {table_name} read successfully.")
            return df
        except Exception as e:
            print(f"Error reading table {table_name}: {e}")
            return None    

    def stop_spark(self):
        self.spark.stop()
        print("Spark session stopped.")