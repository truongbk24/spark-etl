{{ config(order_by='category_key', unique_key='category_key') }}
with category_all as (
    select 
        description
    from {{ source('raw', 'raw_crm_transaction') }}
    union distinct
    select 
        description
    from {{ source('raw', 'raw_sap_transaction') }}
)
select {{ dbt_utils.generate_surrogate_key(['description']) }} AS category_key,
        description
from category_all