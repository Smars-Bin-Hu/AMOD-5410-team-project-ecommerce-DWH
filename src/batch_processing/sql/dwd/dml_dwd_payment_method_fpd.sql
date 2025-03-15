INSERT OVERWRITE TABLE dwd.dwd_payment_method_fpd
SELECT
    payment_method_id,
    payment_method
FROM
    ods.ods_payment_method_fpd;