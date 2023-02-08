import boto3
s3 = boto3.client('s3',
                  endpoint_url='https://is3.cloudhost.id/agungsurya',
                  aws_access_key_id='4J7H6K5L3M2N1O9P8Q7R6S5T',
                  aws_secret_access_key='X9Y8Z7A6B5C4D3E2F1G0H9I8J7K6L5M4N3O2P1Q')

bucket_name = 'agungsurya'
file_name = 'example.txt'
s3.upload_file(file_name, bucket_name, file_name)
