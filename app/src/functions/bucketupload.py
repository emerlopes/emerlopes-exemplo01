import boto3

class S3Upload:
    def __init__(self, access_key, secret_key, bucket_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name

        self.s3 = boto3.client('s3', aws_access_key_id=self.access_key,
                              aws_secret_access_key=self.secret_key)

    def upload_to_s3(self, local_file, s3_file):
        try:
            self.s3.upload_file(local_file, self.bucket_name, s3_file, ExtraArgs={'ContentType': 'application/parquet', 'ACL': 'public-read'})
            print("Upload Successful")
        except FileNotFoundError:
            print("The file was not found")
