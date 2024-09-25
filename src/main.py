import argparse
from jobs.factory_etl import EtlFactory
from common.utils import create_spark_session, get_source_properties
import os

if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Spark Job")
    
    # Add arguments
    parser.add_argument("--source_type", type=str, required=True, help="Source system type to extract the data, such as: mongo, jdbc...")
    parser.add_argument("--source_name", type=str, required=True, help="Source system name to extract the data")
    parser.add_argument("--table_name", type=str, required=True, help="Table name to extract the data")
    
    # Parse arguments
    args = parser.parse_args()
    # Getting argument
    etl_type = args.source_type
    etl_source_system=args.source_name
    etl_source_table=args.table_name
    # spark additional config
    spark_conf_dict = {}
    # get dictionaty from vault
    source_dict = get_source_properties(etl_type)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ge_config_file = os.path.join(script_dir,"config", f'ge_{etl_type}_{etl_source_system}_{etl_source_table}.json')
    if etl_type == 'mongodb':
        mongo_uri_key = source_dict.get(f'mongo_{etl_source_system}_uri_key')
        mongo_uri_value = source_dict.get(f'mongo_{etl_source_system}_uri_value')
        spark_conf_dict[mongo_uri_key] = mongo_uri_value
        spark = create_spark_session(spark_conf_dict)        
        etl = EtlFactory.get_etl(etl_type, spark, database=etl_source_system,collection=etl_source_table, ge_file_name = ge_config_file )
    elif 'jdbc' in etl_type:
        jdbc_url = source_dict.get(f'{etl_type}_{etl_source_system}_url')
        jdbc_username = source_dict.get(f'{etl_type}_{etl_source_system}_username')
        jdbc_password = source_dict.get(f'{etl_type}_{etl_source_system}_password')
        jdbc_driver = source_dict.get('jdbc_driver')
        jdbc_properties = {
            'driver': jdbc_driver,
            'user': jdbc_username,
            'password': jdbc_password
        }
        spark = create_spark_session({})
        etl = EtlFactory.get_etl(etl_type, spark, jdbc_url=jdbc_url,database=etl_source_system, jdbc_properties=jdbc_properties, table_name=etl_source_table, ge_file_name = ge_config_file)

    etl.run()