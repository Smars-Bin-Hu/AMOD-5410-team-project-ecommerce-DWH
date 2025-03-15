INSERT OVERWRITE TABLE dwd.dwd_orders_ipd
SELECT
    order_id_surrogate,
    order_id,
    customer_id,
    DATE_FORMAT(CAST(order_date AS TIMESTAMP), 'yyyy-MM-dd') as order_date,
    campaign_id, -- keep NULL
    amount,
    payment_method_id,
    data_date
FROM
    ods.ods_orders_ipd
WHERE
    data_date = "2025-03-10";