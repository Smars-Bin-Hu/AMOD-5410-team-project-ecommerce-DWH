INSERT OVERWRITE TABLE dws.dws_orders_detailed_info_wide_ipd
SELECT
    ords.order_id,
    ords.customer_id,
    cstm.first_name AS customer_first_name,
    cstm.country AS customer_country,
    ords.order_date,
    ords.order_total_amount, -- INT
    pmt_mthd.payment_method,
--     ords.order_item_id,
    prd.product_id,
    prd.product_name,
    prd.price AS price_per_product, -- decimal(8,2)
    prd.description AS product_desc,
    prd.subcategory_name AS product_subcategory,
    prd.category_name AS product_category,
    ords.item_quantity,
    ords.item_subtotal, -- decimal(10,2)
    ords.item_supplier AS supplier_id,
    spl.supplier_name,
    spl.supplier_email,
    ords.campaign_id,
    cmpn_dscnt.campaign_name,
    cmpn_dscnt.offer_week,
    cmpn_dscnt.discount, -- decimal(8,2)
    ords.item_discount, -- decimal(5,2)
    ords.return_id,
    ords.return_date,
    ords.return_reason,
    ords.amount_refunded, -- decimal(10,2)
    ords.customer_rating_id,
    ords.customer_ratings_by_product, -- decimal(2,1)
    ords.customer_review,
    ords.customer_sentiment,
    ords.data_date -- STRING
FROM
    (SELECT * FROM dwm.dwm_orders_with_items_ipd WHERE data_date = "2025-03-20") ords
        LEFT JOIN
    dim.dim_customer_fpd cstm ON ords.customer_id = cstm.customer_id
        LEFT JOIN
    dim.dim_payment_method_fpd pmt_mthd ON pmt_mthd.payment_method_id = ords.payment_method_id
        LEFT JOIN
    dim.dim_product_fpd prd ON prd.product_id = ords.item_product_id
        LEFT JOIN
    dim.dim_supplier_fpd spl ON spl.supplier_id = ords.item_supplier
        LEFT JOIN
    dim.dim_campaign_discount_fpd cmpn_dscnt ON cmpn_dscnt.campaign_id = ords.campaign_id AND cmpn_dscnt.subcategory_id = prd.subcategory_id
;