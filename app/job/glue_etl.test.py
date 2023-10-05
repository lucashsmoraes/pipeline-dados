import json

# JSON com espaços em branco
json_com_espacos = '''
{
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
'''

# Carregando o JSON em uma variável
json_obj = json.loads(json_com_espacos)

# Convertendo o JSON em uma string sem espaços em branco
json_sem_espacos = json.dumps(json_obj, separators=(',', ':'))

# Verificando o tamanho da string resultante
tamanho_json = len(json_sem_espacos)
if tamanho_json < 256000:
    print("JSON sem espaços em branco: ", json_sem_espacos)
else:
    print("Tamanho do JSON excede o limite de 256 KB.")