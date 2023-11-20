import boto3
import json
import logging

# Configurando o cliente do S3
s3 = boto3.client('s3')

# Configurando o cliente do SQS
sqs = boto3.client('sqs')

# URL da fila do SQS
queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/minha-fila'

# configuração de log
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def enviar_mensagens_sqs(bucket_name, prefix):
    # Listando os objetos do bucket com o prefixo especificado
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    # Verificando se há objetos no bucket
    if 'Contents' in response:
        # Iterando sobre os objetos do bucket
        for obj in response['Contents']:
            # Lendo o arquivo JSON do objeto
            response = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
            json_com_espacos = response['Body'].read().decode('utf-8')

            # Carregando o JSON em uma variável
            json_obj = json.loads(json_com_espacos)

            # Convertendo o JSON em uma string sem espaços em branco
            json_sem_espacos = json.dumps(json_obj, separators=(',', ':'))

            # Convertendo a mensagem para UTF-8
            mensagem = json_sem_espacos.encode('utf-8')

            # Enviando a mensagem para a fila do SQS
            response = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=mensagem
            )

            # Imprimindo a resposta
            logging.info('Mensagem enviada para o SQS: %s', response['MessageId'])
    else:
        logging.warning('Nenhum objeto encontrado no bucket %s com o prefixo %s', bucket_name, prefix)

# Exemplo de uso
enviar_mensagens_sqs('meu-bucket', 'pasta-com-jsons/')