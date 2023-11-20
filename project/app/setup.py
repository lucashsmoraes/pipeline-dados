from setuptools import setup

setup(
    name='app',
    version='0.1',
    author='Lucas Moraes',
    packages=['job_bronze', 'tests', 'data'],
    include_package_data=True,
    install_requires=["pyspark==3.5.0",
                      "boto3==1.18.24",
                      "botocore==1.21.24",
                      "pytest==6.2.4",
                      "pytest-cov==2.12.1",
                      "pandas==1.3.1",
                      "pyarrow==5.0.0",
                      ]
)
