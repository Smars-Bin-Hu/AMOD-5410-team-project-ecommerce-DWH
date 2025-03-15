INSERT OVERWRITE TABLE dwd.dwd_customer_product_ratings_ipd
SELECT
    customerproductrating_id,
    customer_id,
    product_id,
    ratings,
    review,
    sentiment
FROM
    ods.ods_customer_product_ratings_ipd;