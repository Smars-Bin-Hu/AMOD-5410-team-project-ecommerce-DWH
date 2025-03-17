INSERT OVERWRITE TABLE dim.dim_supplier_fpd
SELECT
    supplier_id,
    supplier_name,
    email AS supplier_email
FROM
    dwd.dwd_supplier_fpd;