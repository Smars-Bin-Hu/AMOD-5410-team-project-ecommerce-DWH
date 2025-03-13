-- update partitioned table
MSCK REPAIR TABLE ods.ods_orders_ipd;
MSCK REPAIR TABLE ods.ods_orderitem_ipd;
MSCK REPAIR TABLE ods.ods_customer_product_ratings_ipd;
MSCK REPAIR TABLE ods.ods_returns_ipd;

-- query the loaded tables
select * from ods.ods_returns_ipd;
select * from ods.ods_orders_ipd;
select * from ods.ods_campaign_product_subcategory_fpd;
select * from ods.ods_category_fpd;
select * from ods.ods_customer_fpd;
select * from ods.ods_customer_product_ratings_ipd;
select * from ods.ods_marketing_campaigns_fpd;
select * from ods.ods_orderitem_ipd;
select * from ods.ods_payment_method_fpd;
select * from ods.ods_product_fpd;
select * from ods.ods_subcategory_fpd;
select * from ods.ods_supplier_fpd;
