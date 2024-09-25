select _id as id,
        customer_id as customer_id,
        cast(amount as String) as amount,
        description as description,
        currency as currency,
        transaction_date as transaction_date 
from s3('http://minio:10000/dp-source/crm/transaction/*.parquet','{{ env_var("MINIO_USER") }}','{{ env_var("MINIO_PASSWORD") }}','Parquet')