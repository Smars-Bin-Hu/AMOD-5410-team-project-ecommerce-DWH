INSERT OVERWRITE TABLE dwd.dwd_campaign_product_subcategory_fpd
SELECT
    campaign_product_subcategory_id,
    campaign_id,
    subcategory_id,
    discount
FROM
    ods.ods_campaign_product_subcategory_fpd;