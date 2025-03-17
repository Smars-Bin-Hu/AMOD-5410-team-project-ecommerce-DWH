INSERT OVERWRITE TABLE dim.dim_payment_method_fpd
SELECT
    pmt_mthd.payment_method_id,
    pmt_mthd.payment_method
FROM
    dwd.dwd_payment_method_fpd pmt_mthd;