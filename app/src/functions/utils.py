from src.functions.datalakeingestion import DataLakeIngestion

class Utils:
    def ingestion(table_name):
        host = ''
        database = ''
        user = ''
        password = ''
        access_key = ''
        secret_key = ''
        bucket_name = ''
        file_path = "file_path"
        local_file = "local_file"
        s3_file = ''
        table_name = ''

        data_lake_ingestion = DataLakeIngestion(
            host=host,
            database=database,
            user=user,
            password=password,
            access_key=access_key,
            secret_key=secret_key,
            bucket_name=bucket_name,
            file_path=file_path,
            local_file=local_file,
            s3_file=s3_file)
        
        data_lake_ingestion.data_lake_ingestion(table_name)