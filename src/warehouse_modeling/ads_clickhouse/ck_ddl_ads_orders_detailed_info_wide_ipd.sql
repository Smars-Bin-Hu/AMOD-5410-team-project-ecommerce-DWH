-- Clickhouse DDL
DROP TABLE IF EXISTS ads_data_mart_ecomerce.ads_orders_detailed_info_wide_ipd;
CREATE TABLE IF NOT EXISTS ads_data_mart_ecomerce.ads_orders_detailed_info_wide_ipd
(
    order_id                    UInt128 COMMENT 'Unique identifier for the order',
    customer_id                 UInt128 COMMENT 'Unique identifier for the customer',
    customer_first_name         String COMMENT 'First name of the customer',
    customer_country            String COMMENT 'Country of the customer',
    order_date                  Date COMMENT 'Date when the order was placed',
    order_total_amount          UInt32 COMMENT 'Total amount of the order',

    payment_method              String COMMENT 'Payment method used for the order',

    product_id                  UInt128 COMMENT 'Unique identifier for the product',
    product_name                String COMMENT 'Name of the product',
    price_per_product           Decimal(8, 2) COMMENT 'Unit price of the product',
    product_desc                String COMMENT 'Description of the product',
    product_subcategory         String COMMENT 'Subcategory name of the product',
    product_category            String COMMENT 'Category name of the product',

    item_quantity               UInt32 COMMENT 'Quantity of the item ordered',
    item_subtotal               Decimal(10, 2) COMMENT 'Subtotal amount for this item',

    supplier_id                 UInt32 COMMENT 'Unique identifier for the supplier',
    supplier_name               String COMMENT 'Name of the supplier',
    supplier_email              String COMMENT 'Email of the supplier',

    campaign_id                 Nullable(UInt32) COMMENT 'Unique identifier for the discount campaign',
    campaign_name               Nullable(String) COMMENT 'Name of the discount campaign',
    offer_week                  Nullable(String) COMMENT 'Week in which the campaign offer was active',
    discount                    Nullable(Decimal(8, 2)) COMMENT 'Discount percentage applied',

    item_discount               Decimal(5, 2) COMMENT 'Discount amount for this item',

    return_id                   Nullable(UInt32) COMMENT 'Unique identifier for the return transaction',
    return_date                 Nullable(Date) COMMENT 'Date when the item was returned',
    return_reason               Nullable(String) COMMENT 'Reason for returning the item',
    amount_refunded             Nullable(DECIMAL(10, 2)) COMMENT 'Total refunded amount',

    customer_rating_id          Nullable(UInt32) COMMENT 'Unique identifier for the customer rating',
    customer_ratings_by_product Nullable(Decimal(2, 1)) COMMENT 'Customer rating for the product',
    customer_review             Nullable(String) COMMENT 'Review left by the customer',
    customer_sentiment          Nullable(String) COMMENT 'Customer sentiment analysis result',

    data_date                   Date COMMENT 'Partition key for the table'
) ENGINE = MergeTree()
PARTITION BY toYYYYMMDD(data_date) -- partition based on day
ORDER BY (order_id,product_id);
