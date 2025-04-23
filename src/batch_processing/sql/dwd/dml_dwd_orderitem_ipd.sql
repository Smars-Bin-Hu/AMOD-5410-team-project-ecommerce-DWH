INSERT OVERWRITE TABLE dwd.dwd_orderitem_ipd
SELECT
    orderitem_id,
    order_id,
    product_id,
    quantity,
    supplier_id,
    subtotal,
    discount,
    data_date
FROM
    ods.ods_orderitem_ipd
WHERE
    data_date = "${data_date}";