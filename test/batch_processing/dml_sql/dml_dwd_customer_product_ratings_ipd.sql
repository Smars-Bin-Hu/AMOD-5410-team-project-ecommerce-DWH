INSERT OVERWRITE TABLE dwd.dwd_customer_product_ratings_ipd
SELECT
    customerproductrating_id,
    customer_id,
    product_id,
    ratings,
    review,
    sentiment,
    data_date
FROM
    ods.ods_customer_product_ratings_ipd
WHERE
    data_date = "${data_date}";