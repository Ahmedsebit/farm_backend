import io
import boto3
from datetime import datetime
from flask import current_app


def upload_files(file):
    
    uploaded_folder = current_app.config['AWS_BUCKET_FOLDER']
    
    BUCKET_NAME = current_app.config['AWS_BUCKET_NAME']
    
    ts = str(datetime.utcnow())
    
    filename = file.filename
    file_ext = filename.split(".")
    filename = f'{filename}{ts}.{file_ext[1]}'
    
    s3_resource = boto3.resource(
                        's3',
                        region_name='us-east-1',
                        aws_access_key_id=current_app.config['AWS_ACCESS_ID'],
                        aws_secret_access_key=current_app.config['AWS_SECRET_KEY']
                        )

    response = s3_resource.Object(BUCKET_NAME, filename).put(Body=io.BytesIO(file), Key=f'{uploaded_folder}/{filename}')
    
    if response:
        return filename
    else:
        None