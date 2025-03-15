INSERT OVERWRITE TABLE dwd.dwd_supplier_fpd
SELECT
    supplier_id,
    supplier_name,
    CONCAT(SUBSTRING(email, 1, 1), '***@', SPLIT(email, '@')[1]) as email_mask
FROM
    ods.ods_supplier_fpd;

-- select * from dwd.dwd_supplier_fpd;