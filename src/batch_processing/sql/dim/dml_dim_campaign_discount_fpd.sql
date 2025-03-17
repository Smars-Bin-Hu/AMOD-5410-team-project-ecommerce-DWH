INSERT OVERWRITE TABLE dim.dim_campaign_discount_fpd
SELECT
    cmpn.campaign_id,
    cmpn.campaign_name,
    cmpn_scat.subcategory_id,
    scat.subcategory_name,
    cat.category_id,
    cat.category_name,
    cmpn.offer_week,
    cmpn_scat.discount
FROM 
    dwd.dwd_marketing_campaigns_fpd cmpn
         LEFT JOIN
    dwd.dwd_campaign_product_subcategory_fpd cmpn_scat ON cmpn_scat.campaign_id = cmpn.campaign_id
         LEFT JOIN
    dwd.dwd_subcategory_fpd scat ON scat.subcategory_id = cmpn_scat.subcategory_id
         LEFT JOIN
    dwd.dwd_category_fpd cat ON cat.category_id = scat.category_id
ORDER BY cat.category_id ASC, cmpn_scat.subcategory_id ASC;