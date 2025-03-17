DROP TABLE IF EXISTS dwm.dwm_orders_with_items_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwm.dwm_orders_with_items_ipd
(
    order_id            INT     COMMENT 'Campaign unique id',
    customer_id         STRING  COMMENT 'Campaign name',
    order_date          STRING             COMMENT 'Product subcategory unique id',
    order_total_amount  INT          COMMENT 'Product subcategory name',
    aspayment_method_id INT             COMMENT 'Product category unique id',
    order_item_id       STRING          COMMENT 'Product category name',
    item_product_id     INT             COMMENT 'campaign offering week of the year',
    item_quantity       INT     COMMENT 'discount number for the campaign under this subcategory',
    item_supplier       STRING,
    item_subtotal       DECIMAL(10,2),
    campaign_id         INT,
    item_discount       DECIMAL(5,2),
    return_id           INT,
    return_date         STRING,
    return_reason       STRING,
    amount_refunded     DECIMAL(10,2),
    customer_rating_id  INT,
    customer_ratings_by_product ,
    customer_review,
    customer_sentiment,
    data_date

)
    COMMENT 'DIM Table for campaign information - Daily Full Sync, Permenant Storage'
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dim/dim_campaign_discount_fpd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
