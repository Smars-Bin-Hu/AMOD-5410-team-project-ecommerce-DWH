# build_beeline_command.py

def build_beeline_command(hql: str) -> str:
    cleaned_hql = " ".join(hql.strip().splitlines())  # 把多行合并为一行，保留分号
    return (
        "beeline -u 'jdbc:hive2://hive:10000/default' "
        f"-e \"{cleaned_hql}\""
    )

# if __name__ == '__main__':
#     hql = """
#     MSCK REPAIR TABLE ods.ods_orders_ipd;
#     MSCK REPAIR TABLE ods.ods_orderitem_ipd;
#     MSCK REPAIR TABLE ods.ods_customer_product_ratings_ipd;
#     MSCK REPAIR TABLE ods.ods_returns_ipd;
#     """
#
#     print(build_beeline_command(hql))
