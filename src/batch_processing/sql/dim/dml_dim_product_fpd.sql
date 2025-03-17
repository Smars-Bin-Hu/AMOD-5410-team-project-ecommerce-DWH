INSERT OVERWRITE TABLE dim.dim_product_fpd
SELECT
    prod.product_id AS product_id,
    prod.name AS product_name,
    prod.price AS price,
    prod.descriptiON AS descriptiON,
    prod.subcategory_id AS subcategory_id,
    scat.subcategory_name AS subcategory_name,
    cat.category_id AS category_id,
    cat.category_name AS category_name
FROM
    dwd.dwd_product_fpd prod
        LEFT JOIN
    dwd.dwd_subcategory_fpd scat ON scat.subcategory_id = prod.subcategory_id
        LEFT JOIN
    dwd.dwd_category_fpd cat ON cat.category_id = scat.category_id;