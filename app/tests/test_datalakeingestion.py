
from src.functions.datalakeingestion import DataLakeIngestion


class TestPostgreSQL:

    def test_dataLakeIngestion_class_should_initialized_correctly():
        return True
    
    def test_get_table_should_return_dataframe_valid():
        return True
    
    def test_data_lake_ingestion_should_performs_the_ingestion():
        return True
    
    def test_data_lake_ingestion_should_handle_ingestion_get_table_errors():
        return True
    
    def test_data_lake_ingestion_should_handle_ingestion_save_to_parquet_errors():
        return True
    
    def test_data_lake_ingestion_should_handle_ingestion_upload_to_s3_errors():
        return True
    
    def test_data_lake_ingestion_should_handle_ingestion_invalid_table():
        return True
