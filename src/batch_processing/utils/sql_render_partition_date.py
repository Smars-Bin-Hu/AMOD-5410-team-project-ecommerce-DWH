# Utils - sql render partition date
import re
from datetime import datetime
from typing import Union

DATE_PATTERN = r"\d{4}-\d{2}-\d{2}"  # 格式校验正则

def sql_render_partition_date(
        raw_sql: str,
        data_date: Union[str, datetime],
        placeholder: str = "${data_date}"
)-> str:
    if isinstance(data_date, datetime):
        date_str = data_date.strftime("%Y-%m-%d")
    else:
        date_str = data_date

    if not re.fullmatch(DATE_PATTERN, date_str):
        raise ValueError(f"Invalid date format: {date_str}, expected YYYY-MM-DD")

    sql = raw_sql.replace(placeholder, date_str)

    return sql