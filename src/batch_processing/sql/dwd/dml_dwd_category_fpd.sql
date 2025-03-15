INSERT OVERWRITE TABLE dwd.dwd_category_fpd
SELECT
    category_id,
    category_name
FROM
    ods.ods_category_fpd;