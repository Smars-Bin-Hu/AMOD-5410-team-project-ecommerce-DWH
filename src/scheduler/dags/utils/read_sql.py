import os

def read_sql(file_path : str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(script_dir, file_path)
    abs_path = os.path.normpath(abs_path)

    with open(abs_path, 'r', encoding='utf-8') as file:
        sql = file.read()
    return sql