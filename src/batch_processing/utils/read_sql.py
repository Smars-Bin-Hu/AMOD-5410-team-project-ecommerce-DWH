def read_sql(file_path : str):
    with open(file_path, 'r', encoding='utf-8') as file:
        sql = file.read()
    return sql