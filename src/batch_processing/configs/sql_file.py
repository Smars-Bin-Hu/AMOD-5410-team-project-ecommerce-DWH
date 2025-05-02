sql_dml_files_dwd = \
    {
        "dwd_campaign_product_subcategory_fpd":
            {
                "has_partition": False,
                "path": "../sql/dwd/dml_dwd_campaign_product_subcategory_fpd.sql"
            },
        "dwd_category_fpd":
            {
                "has_partition": False,
                "path": "../sql/dwd/dml_dwd_category_fpd.sql",
            },
        "dwd_customer_fpd":
            {
                "has_partition": False,
                "path":"../sql/dwd/dml_dwd_customer_fpd.sql",
            },
        "dwd_customer_product_ratings_ipd":
            {
                "has_partition": True,
                "path": "../sql/dwd/dml_dwd_customer_product_ratings_ipd.sql",
            },
        "dwd_marketing_campaigns_fpd":
            {
                "has_partition": False,
                "path": "../sql/dwd/dml_dwd_marketing_campaigns_fpd.sql",
            },
        "dwd_orderitem_ipd":
            {
                "has_partition": True,
                "path":  "../sql/dwd/dml_dwd_orderitem_ipd.sql",
            },
        "dwd_orders_ipd":
            {
                "has_partition": True,
                "path": "../sql/dwd/dml_dwd_orders_ipd.sql",
            },
        "dwd_payment_method_fpd":
            {
                "has_partition": False,
                "path":"../sql/dwd/dml_dwd_payment_method_fpd.sql",
            },
        "dwd_product_fpd":
            {
                "has_partition": False,
                "path":"../sql/dwd/dml_dwd_product_fpd.sql",
            },
        "dwd_returns_ipd":
            {
                "has_partition": True,
                "path": "../sql/dwd/dml_dwd_returns_ipd.sql",
            },
        "dwd_subcategory_fpd":
            {
                "has_partition": False,
                "path": "../sql/dwd/dml_dwd_subcategory_fpd.sql",
            },
        "dwd_supplier_fpd":
            {
                "has_partition": False,
                "path": "../sql/dwd/dml_dwd_supplier_fpd.sql",
            }
    }

sql_dml_files_dim = \
    {
        "dim_campaign_discount_fpd":
            {
                "has_partition": False,
                "path":"../sql/dim/dml_dim_campaign_discount_fpd.sql",
            },
        "dim_category_fpd":
            {
                "has_partition": False,
                "path":"../sql/dim/dml_dim_category_fpd.sql",
            },
        "dim_customer_fpd":
            {
                "has_partition": False,
                "path":"../sql/dim/dml_dim_customer_fpd.sql",
            },
        "dim_payment_method_fpd":
            {
                "has_partition": False,
                "path":"../sql/dim/dml_dim_payment_method_fpd.sql",
            },
        "dim_product_fpd":
            {
                "has_partition": False,
                "path":"../sql/dim/dml_dim_product_fpd.sql",
            },
        "dim_supplier_fpd":
            {
                "has_partition": False,
                "path":"../sql/dim/dml_dim_supplier_fpd.sql",
            }
    }

sql_dml_files_dwm = \
    {
        "dwm_campaign_product_subcategory_fpd":
            {
                "has_partition": True,
                "path":"../sql/dwm/dml_dwm_orders_with_items_ipd.sql"
            }
    }

sql_dml_files_dws = \
    {
        "dws_orders_detailed_info_wide_ipd":
            {
                "has_partition": True,
                "path":"../sql/dws/dml_dws_orders_detailed_info_wide_ipd.sql"
            }
    }
