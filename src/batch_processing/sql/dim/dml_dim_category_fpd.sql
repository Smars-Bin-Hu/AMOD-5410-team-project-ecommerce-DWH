INSERT OVERWRITE TABLE dim.dim_category_fpd
SELECT
    cat.category_id,
    cat.category_name,
    scat.subcategory_id,
    scat.subcategory_name
FROM
    dwd.dwd_category_fpd cat
        LEFT JOIN
    dwd.dwd_subcategory_fpd scat ON scat.category_id = cat.category_id
ORDER BY
    category_id,
    subcategory_id ASC;