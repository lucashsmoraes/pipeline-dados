from pyspark.sql.functions import *
from pyspark.sql.types import StructField, StructType, StringType, DoubleType, IntegerType
from pyspark.sql import SparkSession
import os

# Define a estrutura do arquivo
fields = [
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
    StructField("PREMED", StringType(), True),
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
]

def return_schema() -> StructType:
    return StructType(fields)


structure = [
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

# Define as posições iniciais e finais dos campos


# # Cria a transformação para ler o arquivo
# read_fixed_width = glue_context.read.format("csv").schema(schema)\
#                     .load(input_path, positions=positions, header=True, inferSchema=False)

# def show_dataframe() -> DataFrame:
#     # Cria uma sessão Spark
#     spark = SparkSession.builder.appName("Exemplo").getOrCreate()
#
#     schema = StructType(fields)
#     print(schema)
#
#     # Lê o arquivo CSV e cria uma lista de tuplas
#     data = spark.read.csv("C:\\Users\\Pichau\\PycharmProjects\\tcc-pipeline\\app\\job\\COTAHIST_A2022.TXT")
#     df = data.select(
#             substring("_c0", 1, 2),
#             substring("_c0", 3, 8),
#             substring("_c0", 11, 2),
#             substring("_c0", 13, 12),
#             substring("_c0", 25, 3),
#             substring("_c0", 28, 12),
#             substring("_c0", 40, 10),
#             substring("_c0", 50, 3),
#             substring("_c0", 53, 4),
#             substring("_c0", 57, 11),
#             substring("_c0", 70, 11),
#             substring("_c0", 83, 11),
#             substring("_c0", 96, 11),
#             substring("_c0", 109, 11),
#             substring("_c0", 122, 11),
#             substring("_c0", 135, 11),
#             substring("_c0", 148, 5),
#             substring("_c0", 153, 18),
#             substring("_c0", 171, 16),
#             substring("_c0", 189, 11),
#             substring("_c0", 202, 1),
#             substring("_c0", 203, 8),
#             substring("_c0", 211, 7),
#             substring("_c0", 218, 7),
#             substring("_c0", 231, 12),
#             substring("_c0", 243, 3)
#         ).toDF(*structure)
#     return df

def create_session() -> SparkSession:
    path = "C:\\Users\\Pichau\\PycharmProjects\\comparaApi\\GlueTCC_lambda\\Scripts\\python.exe"
    os.environ['PYSPARK_PYTHON'] = path

    return SparkSession.builder.appName("Exemplo").getOrCreate()

def show_dataframe2(spark) -> DataFrame:
    # Cria uma sessão Spark


    schema = StructType(fields)
    print(schema)

    # Lê o arquivo CSV e cria uma lista de tuplas
    data = spark.read.csv("C:\\Users\\Pichau\\PycharmProjects\\tcc-pipeline\\app\\job\\COTAHIST_A2022.TXT")
    return data.select(
            substring("_c0", 1, 2).alias("TIPREG"),
            substring("_c0", 3, 8).alias("DATPRG"),
            substring("_c0", 11, 2).alias("CODBDI"),
            substring("_c0", 13, 12).alias("CODNEG"),
            substring("_c0", 25, 3).alias("TPMERC"),
            substring("_c0", 28, 12).alias("NOMRES"),
            substring("_c0", 40, 10).alias("ESPECI"),
            substring("_c0", 50, 3).alias("PRAZOT"),
            substring("_c0", 53, 4).alias("MODREF"),
            substring("_c0", 57, 11).alias("PREABE"),
            substring("_c0", 70, 11).alias("PREMAX"),
            substring("_c0", 83, 11).alias("PREMIN"),
            substring("_c0", 96, 11).alias("PREMED"),
            substring("_c0", 109, 11).alias("PREULT"),
            substring("_c0", 122, 11).alias("PREOFC"),
            substring("_c0", 135, 11).alias("PREOFV"),
            substring("_c0", 148, 5).alias("TOTNEG"),
            substring("_c0", 153, 18).alias("QUATOT"),
            substring("_c0", 171, 16).alias("VOLTOT"),
            substring("_c0", 189, 11).alias("PREEXE"),
            substring("_c0", 202, 1).alias("INDOPC"),
            substring("_c0", 203, 8).alias("DATVEN"),
            substring("_c0", 211, 7).alias("FATCOT"),
            substring("_c0", 218, 7).alias("PTOEXE"),
            substring("_c0", 231, 12).alias("CODISI"),
            substring("_c0", 243, 3).alias("DISMES")
        )


def do_list(df, schema):
    list = []
    for field in schema:
        if field.dataType != StringType():
            list.append(field.name)
    return list

def verify_type(df, schema):
    for field in schema:
        if field.dataType != StringType():
            df = df.withColumn(field.name, col(field.name).cast(field.dataType))
    return df.toDF(*structure)

def print_list(list):
    for item in list:
        print(item)

def main():
    spark = create_session()
    df = show_dataframe2(spark)
    df.printSchema(1)
    schema = return_schema()
    do_list(df, schema)
    print_list(do_list(df, schema))
    df = verify_type(df, schema)
    df.printSchema(1)
    df.show(3)

if __name__ == "__main__":
    main()
