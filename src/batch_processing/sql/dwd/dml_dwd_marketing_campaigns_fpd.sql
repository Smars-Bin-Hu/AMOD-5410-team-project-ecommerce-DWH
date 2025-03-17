INSERT OVERWRITE TABLE dwd.dwd_marketing_campaigns_fpd
SELECT
    campaign_id,
    campaign_name,
    offer_week
FROM
    ods.ods_marketing_campaigns_fpd;