import pytest
import pandas as pd
from unittest.mock import Mock, MagicMock
from src.functions.datalakeingestion import DataLakeIngestion

class TestDataLakeIngestion:
    datalakeingestion = DataLakeIngestion()
    def setup_method(self):
        self.mock_postgresql = MagicMock()
        self.dli = DataLakeIngestion(
            host="test_host",
            database="test_database",
            user="test_user",
            password="test_password"
        )
        self.dli.postgresql = self.mock_postgresql

    
    @pytest.fixture
    def data_lake_ingestion(self):
        return DataLakeIngestion(
            host='host',
            database='database',
            user='user',
            password='password',
            access_key='access_key',
            secret_key='secret_key',
            bucket_name='bucket_name',
            file_path='file_path',
            local_file='local_file',
            s3_file='s3_file'
        )

    def test_data_lake_ingestion(self, data_lake_ingestion):
        # Mocking the PostgreSQL object
        postgresql = Mock()
        postgresql.get_table_as_dataframe.return_value = 'dataframe'
        data_lake_ingestion.get_table = Mock(return_value=postgresql.get_table_as_dataframe.return_value)

        # Mocking the ParquetFile object
        parquet_file = Mock()
        data_lake_ingestion.file_path = 'file_path'
        data_lake_ingestion.parquet_file = parquet_file

        # Mocking the S3Upload object
        s3_upload = Mock()
        data_lake_ingestion.access_key = 'access_key'
        data_lake_ingestion.secret_key = 'secret_key'
        data_lake_ingestion.bucket_name = 'bucket_name'
        data_lake_ingestion.local_file = 'local_file'
        data_lake_ingestion.s3_file = 's3_file'
        data_lake_ingestion.s3_upload = s3_upload

        # Call the data_lake_ingestion method
        data_lake_ingestion.data_lake_ingestion(0)

        # Assertions
        postgresql.get_table_as_dataframe.assert_called_once_with("SELECT * FROM 0")
        parquet_file.save_to_parquet.assert_called_once_with('dataframe')
        s3_upload.upload_to_s3.assert_called_once_with(
            local_file='local_file',
            s3_file='s3_file'
        )        
        
    def test_get_table_valid(self):
        # Test with a valid table name
        self.mock_postgresql.get_table_as_dataframe.return_value = pd.DataFrame()
        df = self.dli.get_table(0)
        self.mock_postgresql.get_table_as_dataframe.assert_called_with("SELECT * FROM 0")
        assert isinstance(df, pd.DataFrame)
        
    def test_get_table_invalid(self):
        # Test with an invalid table name
        with pytest.raises(ValueError):
            self.dli.get_table(2)
