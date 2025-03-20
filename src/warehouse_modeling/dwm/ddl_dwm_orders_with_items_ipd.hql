DROP TABLE IF EXISTS dwm.dwm_orders_with_items_ipd;
CREATE EXTERNAL TABLE IF NOT EXISTS dwm.dwm_orders_with_items_ipd
(
    order_id                    INT             COMMENT 'Order unique id',
    customer_id                 INT             COMMENT 'Customer ordered',
    order_date                  STRING          COMMENT 'The date the customer ordered',
    order_total_amount          INT             COMMENT 'The total amount paid of the order',
    payment_method_id           INT             COMMENT 'Payment method id',
    order_item_id               STRING          COMMENT 'The item id under this order',
    item_product_id             INT             COMMENT 'The product of the item',
    item_quantity               INT             COMMENT 'The number of products under this order ',
    item_supplier               INT             COMMENT 'The supplier provide the item',
    item_subtotal               DECIMAL(10,2)   COMMENT 'The subtotal amount for the item',
    campaign_id                 INT             COMMENT 'The campaign id for current order',
    item_discount               DECIMAL(5,2)    COMMENT 'The discount for the item got',
    return_id                   INT             COMMENT 'The return id for the item',
    return_date                 STRING          COMMENT 'The return date for the item',
    return_reason               STRING          COMMENT 'The return reason for the item',
    amount_refunded             DECIMAL(10,2)   COMMENT 'The amount refunded to the customer for the item',
    customer_rating_id          INT             COMMENT 'The id of rating given by the customer for the item',
    customer_ratings_by_product DECIMAL(2,1)    COMMENT 'The rating given by the customer for the item',
    customer_review             STRING          COMMENT 'The review given by the customer',
    customer_sentiment          STRING          COMMENT 'The sentiment given by the customer'
)
    COMMENT 'DWM Table for orders with items information - Daily Increment Sync, Permenant Storage'
    PARTITIONED BY (data_date STRING COMMENT 'partition field')
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dwm/dwm_orders_with_items_ipd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
