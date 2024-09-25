	
{{ config(unique_key=['category_key','customer_key','date_key']) }}
select category_key as category_key,
		customer_key as customer_key, 
		date_key as date_key,
		count(id) as total_volume,
		sum(amount) as total_amount
from
	(select dc.category_key,
			dc2.customer_key,
			toUInt64(formatDateTime(rst.transaction_date, '%Y%m%d')) as date_key,
			rst.id,
			toFloat64(rst.amount) as amount,
			rst.transaction_date 
	from datamart.dim_category dc inner join raw.raw_sap_transaction rst on dc.description = rst.description 
									inner join datamart.dim_customer dc2 on rst.customer_id = dc2.code and dc2.`source` ='sap'		
	union all
	select dc.category_key,
			dc2.customer_key,
			toUInt64(formatDateTime(rct.transaction_date, '%Y%m%d')),
			rct.id,
			toFloat64(rct.amount),
			rct.transaction_date 
	from datamart.dim_category dc inner join raw.raw_crm_transaction rct on dc.description = rct.description 
									inner join datamart.dim_customer dc2 on rct.customer_id = dc2.code and dc2.`source` ='crm')
group by category_key,
		customer_key, 
		date_key