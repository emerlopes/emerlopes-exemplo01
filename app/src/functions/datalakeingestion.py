from src.functions.postgresql import PostgreSQL
from src.functions.parquetfile import ParquetFile
from src.functions.bucketupload import S3Upload


class DataLakeIngestion:
    def __init__(self, host, database, user, password, access_key, secret_key, bucket_name, file_path, local_file, s3_file):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.file_path = file_path
        self.local_file = local_file
        self.s3_file = s3_file

    def data_lake_ingestion(self, table_name):
        try:
            # Get table in dataframe
            df = self.get_table(table_name)

            # Save the data to a parquet file
            parquet_file = ParquetFile(file_path=self.file_path)
            parquet_file.save_to_parquet(df)

            # Upload the file to S3
            s3_upload = S3Upload(
                access_key=self.access_key,
                secret_key=self.secret_key,
                bucket_name=self.bucket_name)

            s3_upload.upload_to_s3(
                local_file=self.local_file,
                s3_file=self.s3_file)

        except Exception as e:
            print("Error while data lake ingestion: ", e)

    def get_table(self, table_name):
        # Get the data from PostgreSQL
        postgresql = PostgreSQL(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password)
        
        try:
            if table_name == 0:
                df = postgresql.get_table_as_dataframe(f"SELECT * FROM {table_name}")
            elif table_name == 1:
                df = postgresql.get_table_as_dataframe(f"SELECT * FROM {table_name}")
            else:
                raise ValueError("Invalid table name")
        except Exception as e:
            print("Error while fetching data from the table: ", e)
            
        return df
