select _id as id,
        name,
        email
from s3('http://minio:10000/dp-source/crm/customer/*.parquet','{{ env_var("MINIO_USER") }}','{{ env_var("MINIO_PASSWORD") }}','Parquet')