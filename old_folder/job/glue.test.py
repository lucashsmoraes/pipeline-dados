from pyspark.sql.functions import *
from pyspark.sql.types import StructField, StructType, StringType, DoubleType, IntegerType
from pyspark.sql import SparkSession
import os
from datetime import datetime

PATH_ORIGEM = "C:\\Users\\Pichau\\PycharmProjects\\tcc-pipeline\\app\\job\\COTAHIST_A2022.TXT"
def create_session() -> SparkSession:
    return SparkSession.builder.appName("JOB").getOrCreate()

def return_schema() -> StructType:
    return StructType([
        StructField("TIPREG", StringType(), True),
        StructField("DATPRG", StringType(), True),
        StructField("CODBDI", StringType(), True),
        StructField("CODNEG", StringType(), True),
        StructField("TPMERC", IntegerType(), True),
        StructField("NOMRES", StringType(), True),
        StructField("ESPECI", StringType(), True),
        StructField("PRAZOT", StringType(), True),
        StructField("MODREF", StringType(), True),
        StructField("PREABE", DoubleType(), True),
        StructField("PREMAX", DoubleType(), True),
        StructField("PREMIN", DoubleType(), True),
        StructField("PREMED", DoubleType(), True),
        StructField("PREULT", DoubleType(), True),
        StructField("PREOFC", DoubleType(), True),
        StructField("PREOFV", DoubleType(), True),
        StructField("TOTNEG", IntegerType(), True),
        StructField("QUATOT", IntegerType(), True),
        StructField("VOLTOT", DoubleType(), True),
        StructField("PREEXE", DoubleType(), True),
        StructField("INDOPC", StringType(), True),
        StructField("DATVEN", StringType(), True),
        StructField("FATCOT", IntegerType(), True),
        StructField("PTOEXE", DoubleType(), True),
        StructField("CODISI", StringType(), True),
        StructField("DISMES", IntegerType(), True)
    ])

def return_columns_names() -> list:
    return [
        "tipo_de_registro",
        "data_pregao",
        "codigo_bdi",
        "codigo_negociacao",
        "tipo_mercado",
        "nome_resumido",
        "especificacao",
        "prazo_termo",
        "moeda_referencia",
        "preco_abertura",
        "preco_maximo",
        "preco_minimo",
        "preco_medio",
        "preco_ultimo",
        "preco_melhor_oferta_compra",
        "preco_melhor_oferta_venda",
        "numero_negocios",
        "quantidade_titulos_negociados",
        "volume_negocios",
        "preco_exercicio_opcoes",
        "indicador_correcao_preco",
        "data_vencimento_opcoes",
        "fator_cotacao",
        "preco_exercicio_pontos",
        "codigo_papel",
        "numero_distribuicao"
    ]


def load_file(spark) -> DataFrame:
    df = spark.read.text(PATH_ORIGEM)
    print(df.show(3))
    return df
def create_dataframe(spark, data) -> DataFrame:
    return data.select(
        substring("value", 1, 2).alias("TIPREG"),
        substring("value", 3, 8).alias("DATPRG"),
        substring("value", 11, 2).alias("CODBDI"),
        substring("value", 13, 12).alias("CODNEG"),
        substring("value", 25, 3).alias("TPMERC"),
        substring("value", 28, 12).alias("NOMRES"),
        substring("value", 40, 10).alias("ESPECI"),
        substring("value", 50, 3).alias("PRAZOT"),
        substring("value", 53, 4).alias("MODREF"),
        substring("value", 57, 11).alias("PREABE"),
        substring("value", 70, 11).alias("PREMAX"),
        substring("value", 83, 11).alias("PREMIN"),
        substring("value", 96, 11).alias("PREMED"),
        substring("value", 109, 11).alias("PREULT"),
        substring("value", 122, 11).alias("PREOFC"),
        substring("value", 135, 11).alias("PREOFV"),
        substring("value", 148, 5).alias("TOTNEG"),
        substring("value", 153, 18).alias("QUATOT"),
        substring("value", 171, 16).alias("VOLTOT"),
        substring("value", 189, 11).alias("PREEXE"),
        substring("value", 202, 1).alias("INDOPC"),
        substring("value", 203, 8).alias("DATVEN"),
        substring("value", 211, 7).alias("FATCOT"),
        substring("value", 218, 7).alias("PTOEXE"),
        substring("value", 231, 12).alias("CODISI"),
        substring("value", 243, 3).alias("DISMES")
    )



def list_not_string(df, schema):
    list = []
    for field in schema:
        if field.dataType != StringType():
            list.append(field.name)
    return list

def verify_type_to_cast(df, schema):
    for field in schema:
        if field.dataType != StringType():
            df = df.withColumn(field.name, col(field.name).cast(field.dataType))
    return df.toDF(*return_columns_names())


def print_list(list):
    for item in list:
        print(item)


def main():
    time = datetime.now()
    print("inicio", time)
    spark = create_session()
    data = load_file(spark)
    df = create_dataframe(spark, data)
    df.printSchema(1)

    schema = return_schema()

    list = list_not_string(df, schema)
    print_list(list)

    df = verify_type_to_cast(df, schema)
    df.printSchema(1)
    df.show(3)
    time = datetime.now()
    print("fim", time)


if __name__ == "__main__":
    main()
