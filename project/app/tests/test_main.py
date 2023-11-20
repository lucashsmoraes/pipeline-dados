import unittest
from pyspark.testing.utils import assertDataFrameEqual
from pyspark.sql import SparkSession
from job_bronze.main import create_dataframe, return_columns_names, return_schema, verify_type_to_cast, \
    list_not_string, load_file


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.appName("Test").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()


# Define unit tests class
class Test(TestBase):
    # Define unit test methods

    def test_return_schema(self):
        # Define expected result
        expected = return_schema()
        # Define actual result
        actual = return_schema()
        # Compare expected and actual results
        self.assertEqual(expected, actual)

    def test_return_columns_names(self):
        # Define expected result
        expected = return_columns_names()[0]
        self.assertEqual(expected, "tipo_de_registro")

    def test_create_dataframe(self):
        data = self.read_file
        dataframe = create_dataframe(data)
        expected = len(dataframe.columns)
        self.assertEqual(expected, 26)

    def test_verify_type_to_cast(self):
        data = self.read_file
        # Define expected result
        expected = verify_type_to_cast(create_dataframe(data), return_schema())
        # Define actual result
        actual = verify_type_to_cast(create_dataframe(data), return_schema())
        # Compare expected and actual results
        assertDataFrameEqual(expected, actual)

    def test_list_not_string(self):
        # Define expected result
        expected = list_not_string(return_schema())
        # Define actual result
        actual = ['TPMERC', 'PREABE', 'PREMAX', 'PREMIN', 'PREMED', 'PREULT', 'PREOFC', 'PREOFV', 'TOTNEG', 'QUATOT',
                  'VOLTOT', 'PREEXE', 'FATCOT', 'PTOEXE', 'DISMES']
        # Compare expected and actual results
        self.assertEqual(expected, actual)

    @property
    def read_file(self):
        return load_file(self.spark, "../data/COTAHIST_A2022.TXT")
