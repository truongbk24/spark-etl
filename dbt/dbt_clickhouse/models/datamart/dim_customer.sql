{{ config(order_by='customer_key', unique_key='customer_key') }}
with customer_all as (
    select 
        id as code,
        name,
        email,
        'sap' as source
    from {{ source('raw', 'raw_sap_customer') }}
    union all
    select 
        id as code,
        name,
        email,
        'crm' as source
    from {{ source('raw', 'raw_crm_customer') }}
)
select {{ dbt_utils.generate_surrogate_key(['code', 'name', 'email', 'source']) }} AS customer_key,
        code,
        name,
        email,
        source
from customer_all