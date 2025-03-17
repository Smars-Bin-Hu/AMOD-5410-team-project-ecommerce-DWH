INSERT OVERWRITE TABLE dim.dim_customer_fpd
SELECT
    cstm.customer_id,
    cstm.first_name,
    cstm.last_name,
    cstm.email AS customer_email,
    cstm.country
FROM
    dwd.dwd_customer_fpd cstm;