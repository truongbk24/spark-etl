{{ config(order_by='date_key', unique_key='date_key') }}
-- models/date_dimension.sql
WITH
    toStartOfDay(toDate('2020-01-01')) AS start,
    toStartOfDay(toDate('2030-12-31')) AS end
SELECT
	toUInt64(formatDateTime(date, '%Y%m%d')) as date_key, 
    date,
    toYear(date) AS year,
    toMonth(date) AS month,
    toDayOfMonth(date) AS day_of_month,
    toDayOfWeek(date) AS day_of_week,   -- 1 = Monday, ..., 7 = Sunday
    toDayOfYear(date) AS day_of_year,
    toISOWeek(date) AS week,
    if(toDayOfWeek(date) IN (6, 7), 1, 0) AS is_weekend,  -- 1 if Saturday or Sunday
    toQuarter(date) AS quarter,
    formatDateTime(date, '%Y-%m') AS year_month,
    formatDateTime(date, '%Y-W%V') AS year_week
FROM
(
	SELECT arrayJoin(arrayMap(x -> toDate(x), range(toUInt32(start), toUInt32(end), 24 * 3600))) as date
)
ORDER BY date