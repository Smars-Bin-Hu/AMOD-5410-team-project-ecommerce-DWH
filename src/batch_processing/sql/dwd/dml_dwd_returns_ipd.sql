INSERT OVERWRITE TABLE dwd.dwd_returns_ipd
SELECT
    return_id,
    order_id,
    product_id,
    return_date,
    reason,
    amount_refunded,
    data_date
FROM
    ods.ods_returns_ipd
WHERE
    data_date = "2025-03-10";