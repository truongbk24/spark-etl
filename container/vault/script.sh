VAULT_ADDR='http://vault:8200'
VAULT_TOKEN="root"
# Export environment variables
export VAULT_ADDR
export VAULT_TOKEN
# Check if Vault is initialized and unsealed
vault status
# init key value for mongo and mysql
vault kv put secret/mongodb mongo_crm_uri_key="spark.mongodb.read.connection.uri" mongo_crm_uri_value="mongodb://mongodb:27017"
vault kv put secret/jdbc_mysql jdbc_mysql_sap_url="jdbc:mysql://mysql:3306/sap" jdbc_mysql_sap_username="user" jdbc_mysql_sap_password="123456"
vault kv put secret/spark/config spark.hadoop.fs.s3a.endpoint="http://minio:10000" spark.hadoop.fs.s3a.access.key="minioadmin" spark.hadoop.fs.s3a.secret.key="minioadmin" spark.hadoop.fs.s3a.impl="org.apache.hadoop.fs.s3a.S3AFileSystem" spark.hadoop.fs.s3a.path.style.access="true" spark.hadoop.fs.s3a.connection.ssl.enabled="false" spark.dynamicAllocation.enabled="false"

vault kv get secret/spark/config
