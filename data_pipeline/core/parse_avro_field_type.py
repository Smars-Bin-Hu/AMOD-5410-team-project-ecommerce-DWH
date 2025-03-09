
from pyspark.sql.types import (
    IntegerType, StringType, DecimalType, DateType, FloatType, DoubleType, LongType
)

def parse_avro_type(avro_type_def):
    """
    解析 avro_type_def (可能是 str / list / dict)，返回Spark可用的 DataType 对象。
    """
    # 1) 如果是简单字符串，比如 "int", "string", "long" ...
    if isinstance(avro_type_def, str):
        avro_type_def = avro_type_def.lower()
        if avro_type_def == "int":
            return IntegerType()
        elif avro_type_def == "long":
            return LongType()
        elif avro_type_def == "float":
            return FloatType()
        elif avro_type_def == "double":
            return DoubleType()
        elif avro_type_def == "string":
            return StringType()
        # 其他：bool、bytes 等根据需要做映射
        else:
            # 默认使用 StringType，或者抛出异常
            return StringType()

    # 2) 如果是 list，常见形式 ["null", "string"] 之类
    elif isinstance(avro_type_def, list):
        # 只要找到其中非 "null" 的类型即可
        # 比如 ["null", "string"] => StringType
        non_null_types = [t for t in avro_type_def if t != "null"]
        if not non_null_types:
            # 全是 null？默认 String
            return StringType()
        # 取第一个非 null 的类型继续解析 (可能还是 str/dict)
        return parse_avro_type(non_null_types[0])

    # 3) 如果是 dict，例如 {"type":"bytes", "logicalType":"decimal", "precision":2, "scale":1}
    elif isinstance(avro_type_def, dict):
        # 3.1) 解析 decimal
        if avro_type_def.get("logicalType") == "decimal":
            precision = avro_type_def.get("precision", 38)
            scale = avro_type_def.get("scale", 0)
            return DecimalType(precision, scale)
        # 3.2) 解析 date
        elif avro_type_def.get("logicalType") == "date":
            # Avro "date" 通常存储成 int 或 string, 这里可自定义
            # 你若想保留原始 string, 可以 return StringType()
            # 如果你想用 Spark 的 DateType, 看文件实际存储情况
            return DateType()

        # 3.3) 若 dict 里有 "type": "string"/"int"/"bytes" 等，再递归解析
        # if "type" in avro_type_def:
        #     return parse_avro_type(avro_type_def["type"])

        # 其他情况，fallback
        return StringType()

    # 4) fallback: 不认识的情况
    return StringType()
