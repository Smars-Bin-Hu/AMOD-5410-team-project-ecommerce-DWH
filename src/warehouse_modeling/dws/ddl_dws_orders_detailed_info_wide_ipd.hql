DROP TABLE IF EXISTS dws.dws_orders_detailed_info_wide_ipd;
CREATE TABLE IF NOT EXISTS dws.dws_orders_detailed_info_wide_ipd
(
    order_id                    INT COMMENT 'Unique identifier for the order',
    customer_id                 INT COMMENT 'Unique identifier for the customer',
    customer_first_name         STRING COMMENT 'First name of the customer',
    customer_country            STRING COMMENT 'Country of the customer',
    order_date                  STRING COMMENT 'Date when the order was placed',
    order_total_amount          INT COMMENT 'Total amount of the order',

    payment_method              STRING COMMENT 'Payment method used for the order',

    product_id                  INT COMMENT 'Unique identifier for the product',
    product_name                STRING COMMENT 'Name of the product',
    price_per_product           DECIMAL(8, 2) COMMENT 'Unit price of the product',
    product_desc                STRING COMMENT 'Description of the product',
    product_subcategory         STRING COMMENT 'Subcategory name of the product',
    product_category            STRING COMMENT 'Category name of the product',

    item_quantity               INT COMMENT 'Quantity of the item ordered',
    item_subtotal               DECIMAL(10, 2) COMMENT 'Subtotal amount for this item',

    supplier_id                 INT COMMENT 'Unique identifier for the supplier',
    supplier_name               STRING COMMENT 'Name of the supplier',
    supplier_email              STRING COMMENT 'Email of the supplier',

    campaign_id                 INT COMMENT 'Unique identifier for the discount campaign',
    campaign_name               STRING COMMENT 'Name of the discount campaign',
    offer_week                  STRING COMMENT 'Week in which the campaign offer was active',
    discount                    DECIMAL(8, 2) COMMENT 'Discount percentage applied',

    item_discount               DECIMAL(5, 2) COMMENT 'Discount amount for this item',

    return_id                   INT COMMENT 'Unique identifier for the return transaction',
    return_date                 STRING COMMENT 'Date when the item was returned',
    return_reason               STRING COMMENT 'Reason for returning the item',
    amount_refunded             DECIMAL(10, 2) COMMENT 'Total refunded amount',

    customer_rating_id          INT COMMENT 'Unique identifier for the customer rating',
    customer_ratings_by_product DECIMAL(2, 1) COMMENT 'Customer rating for the product',
    customer_review             STRING COMMENT 'Review left by the customer',
    customer_sentiment          STRING COMMENT 'Customer sentiment analysis result'
)
    COMMENT 'DWS table for orders with detailed information joined with dws tables - Daily Increment Sync, Permenant Storage'
    PARTITIONED BY (data_date STRING COMMENT 'partition field')
    STORED AS PARQUET
    LOCATION '/user/hive/warehouse/dws/dws_orders_detailed_info_wide_ipd'
    TBLPROPERTIES (
        "parquet.compress" = "SNAPPY",
        "transactional" = "false", -- Hive transaction usually are ORC file format, so prevent here.
        'parquet.timestamp.skip.conversion' = 'false' -- Spark and Hive timestamp convertion compatible
        );
