INSERT OVERWRITE TABLE dwd.dwd_subcategory_fpd
SELECT
    subcategory_id,
    subcategory_name,
    category_id
FROM
    ods.ods_subcategory_fpd;
