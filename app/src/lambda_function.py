from src.functions.utils import Utils

def lambda_handler(event, context):
    data_lake = Utils()
    
    data_lake.ingestion("table_0")
