-- ods
MSCK REPAIR TABLE ods.ods_orders_ipd;
MSCK REPAIR TABLE ods.ods_orderitem_ipd;
MSCK REPAIR TABLE ods.ods_customer_product_ratings_ipd;
MSCK REPAIR TABLE ods.ods_returns_ipd;

-- dwd
MSCK REPAIR TABLE dwd.dwd_orders_ipd;
MSCK REPAIR TABLE dwd.dwd_orderitem_ipd;
MSCK REPAIR TABLE dwd.dwd_customer_product_ratings_ipd;
MSCK REPAIR TABLE dwd.dwd_returns_ipd;

-- dwm
MSCK REPAIR TABLE dwm.dwm_orders_with_items_ipd;

-- dws
MSCK REPAIR TABLE dws.dws_orders_detailed_info_wide_ipd;