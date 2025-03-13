from pyspark.sql.types import *
import re

SPARK_TYPE_MAPPING = {
    "int": IntegerType(),
    "long": LongType(),
    "float": FloatType(),
    "double": DoubleType(),
    "string": StringType(),
    "boolean": BooleanType(),
    "binary": BinaryType(),
    "date": DateType(),
}

def parse_field_type(field_type):
    """
    解析字段映射，返回 Spark DataType。
    支持基本类型、decimal(x,y)、date 类型。
    """
    field_type = field_type.lower().strip()

    # 解析 decimal(precision, scale)
    if field_type.startswith("decimal"):
        match = re.match(r"decimal\((\d+),\s*(\d+)\)", field_type)
        if match:
            precision, scale = map(int, match.groups())
            return DecimalType(precision, scale)

    # 直接匹配 Spark 类型
    return SPARK_TYPE_MAPPING.get(field_type, StringType())  # 默认 StringType