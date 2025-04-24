def read_sql(file_path : str):
    with open(file_path, 'r', encoding='utf-8') as file:
        sql = file.read()
    return sql

if __name__ == '__main__':
    print(read_sql('./dml_sql/dml_dwd_customer_product_ratings_ipd.sql'))