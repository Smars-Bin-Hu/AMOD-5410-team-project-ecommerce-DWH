INSERT OVERWRITE TABLE dwd.dwd_product_fpd
SELECT
    product_id,
    name,
    price,
    description,
    subcategory_id
FROM
    ods.ods_product_fpd;