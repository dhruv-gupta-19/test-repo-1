import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Create a new S3 bucket
s3.create_bucket(Bucket='my-new-bucket')
