import fastparquet

class ParquetFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_to_parquet(self, df):
        fastparquet.write(self.file_path, df, compression='GZIP')
        print("Data saved to parquet file successfully")
