select cast(id as String) as id,
        cast(customer_id as String) as customer_id,
        cast(amount as String) as amount,
        currency as currency,
        transaction_date as transaction_date,
        description as description
from s3('http://minio:10000/dp-source/sap/transaction/*.parquet','{{ env_var("MINIO_USER") }}','{{ env_var("MINIO_PASSWORD") }}','Parquet')