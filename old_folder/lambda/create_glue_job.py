import boto3
import os

glue = boto3.client('glue')

role_glue = os.environ['ROLE_GLUE']

def lambda_handler(event, context):
    response = glue.create_job(
        Name='tcc-glue',
        Role= role_glue,
        Command={
            'Name': 'glueetl',
            'ScriptLocation': 's3://tcc-script/job1/glue-etl.py'
        },
        DefaultArguments={
            '--job-bookmark-option': 'job-bookmark-enable',
            '--additional-python-modules': 'delta-spark==1.0.0',
            '--extra-jars': 's3://tcc-script/jars/delta-core_2.12-1.0.0.jar',
            '--conf spark.delta.logStore.class': 'org.apache.spark.sql.delta.storage.S3SingleDriverLogStore',
            '--conf spark.sql.extensions': 'io.delta.sql.DeltaSparkSessionExtension'
        },
        MaxRetries=0,
        AllocatedCapacity=2,
        Timeout=60,
        MaxCapacity=10,
        WorkerType='G.1X',
        NumberOfWorkers=5
    )
    return response
