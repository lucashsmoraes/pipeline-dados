import os

from pyspark.shell import sc
from pyspark.sql import SparkSession
import json



# Dados cadastrais
dados_cadastrais = {
    "id": 1,
    "nome": "João da Silva",
    "data_nascimento": "01/01/1990",
    "cpf": "123.456.789-00",
    "endereco": {
        "cidade": "São Paulo",
        "rua": "Rua A",
        "cep": "12345-678",
        "uf": "SP",
        "bairro": "Centro",
        "numero": "123"
    },
    "telefone": [
        {
            "tipo": "residencial",
            "telefone": "1234-5678",
            "ddd": "11"
        },
        {
            "tipo": "celular",
            "telefone": "98765-4321",
            "ddd": "11"
        }
    ],
    "email": [
        {
            "email": "joao.silva@gmail.com",
            "data_atualizacao": "01/01/2021"
        },
        {
            "email": "joao.silva@hotmail.com",
            "data_atualizacao": "01/01/2021"
        }
    ]
}

if __name__ == '__main__':


    # Configurando a sessão do Spark
    spark = SparkSession.builder.appName("Exemplo").getOrCreate()

    path = "C:\\Users\\Pichau\\PycharmProjects\\comparaApi\\GlueTCC_lambda\\Scripts\\python.exe"
    os.environ['PYSPARK_PYTHON'] = path

    # Convertendo para JSON
    dados_cadastrais_json = json.dumps(dados_cadastrais)

    # Lendo o JSON com PySpark
    df = spark.read.json(sc.parallelize([dados_cadastrais_json]))

    # Imprimindo o DataFrame
    df.show()