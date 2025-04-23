INSERT OVERWRITE TABLE dwd.dwd_returns_ipd
SELECT
    return_id,
    order_id,
    product_id,
    DATE_FORMAT(CAST(return_date AS TIMESTAMP), 'yyyy-MM-dd') as order_date,
    reason,
    amount_refunded,
    data_date
FROM
    ods.ods_returns_ipd
WHERE
    data_date = "${data_date}";