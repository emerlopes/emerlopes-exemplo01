
from src.functions.bucketupload import S3Upload
import boto3
import pytest


class TestBucketUpload:

    def test_S3Upload_class_should_initialized_correctly(self):
        access_key = "ACCESS_KEY"
        secret_key = "SECRET_KEY"
        bucket_name = "BUCKET_NAME"
    
        uploader = S3Upload(access_key, secret_key, bucket_name)
    
        assert uploader.access_key == access_key
        assert uploader.secret_key == secret_key
        assert uploader.bucket_name == bucket_name
    
    def test_upload_to_s3_should_send_file_to_bucket():
        return True
        
    def test_upload_to_s3_should_handle_file_not_found():
        return True
