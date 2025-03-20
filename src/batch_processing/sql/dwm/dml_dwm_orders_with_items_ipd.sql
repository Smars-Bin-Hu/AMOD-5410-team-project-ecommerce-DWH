INSERT OVERWRITE TABLE dwm.dwm_orders_with_items_ipd
SELECT
    ords.order_id AS order_id,
    ords.customer_id AS customer_id,
    ords.order_date AS order_date, -- could get the week of year
    ords.amount AS order_total_amount,
    ords.payment_method_id AS payment_method_id ,
    ords_itm.orderitem_id AS order_item_id,
    ords_itm.product_id AS item_product_id,
    ords_itm.quantity AS item_quantity,
    ords_itm.supplier_id AS item_supplier,
    ords_itm.subtotal AS item_subtotal,
    ords.campaign_id AS campaign_id,
    ords_itm.discount AS item_discount,
    rets.return_id AS return_id,
    rets.return_date AS return_date,
    rets.reason AS return_reASON,
    rets.amount_refunded AS amount_refunded,
    rts.customerproductrating_id AS customer_rating_id,
    rts.ratings AS customer_ratings_by_product,
    rts.review AS customer_review,
    rts.sentiment AS customer_sentiment,
    ords.data_date
FROM
    (SELECT * FROM dwd.dwd_orders_ipd WHERE data_date = "2025-03-20") ords
        LEFT JOIN
    (SELECT * FROM dwd.dwd_orderitem_ipd WHERE data_date = "2025-03-20") ords_itm ON ords.order_id = ords_itm.order_id
        LEFT JOIN
    (SELECT * FROM dwd.dwd_returns_ipd WHERE data_date = "2025-03-20") rets ON rets.order_id = ords.order_id AND rets.product_id = ords_itm.product_id
        LEFT JOIN
    (SELECT * FROM dwd.dwd_customer_product_ratings_ipd WHERE data_date = "2025-03-20") rts ON rts.customer_id = ords.customer_id AND rts.product_id = ords_itm.product_id
;