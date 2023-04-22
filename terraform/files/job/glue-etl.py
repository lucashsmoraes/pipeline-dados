from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    year,
    month,
    dayofmonth,
    hour,
    weekofyear,
    dayofweek,
    udf,
    col,
    row_number,
    monotonically_increasing_id
)

from pyspark.sql import types as T
from pyspark.sql import Window
from datetime import datetime


def create_spark_session():
    spark = SparkSession.builder.getOrCreate()
    return spark


def main():
    spark = create_spark_session()
    input_data = "s3://tcc-origem-469691162657/"
    output_data = "s3://tcc-processados-469691162657/"


if __name__ == "__main__":
    main()
