INSERT OVERWRITE TABLE dwd.dwd_customer_fpd
SELECT
    customer_id,
    CONCAT(SUBSTRING(first_name, 1, 2), REPEAT('*', LENGTH(first_name)-2)) as first_name_mask,
    MD5(last_name) last_name_mask,
    CONCAT(SUBSTRING(email, 1, 1), '***@', SPLIT(email, '@')[1]) as email_mask,
    country
FROM
    ods.ods_customer_fpd;