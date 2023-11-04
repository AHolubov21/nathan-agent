import boto3
import json

class LambdaModule:

    def __init__(self, access_key, secret_key, region_name='us-west-2'):
        self.client = boto3.client(
            'lambda',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region_name
        )

    def create_lambda_function(self, function_name, role, handler, zip_file):
        with open(zip_file, 'rb') as f:
            zipped_code = f.read()

        response = self.client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role=role,
            Handler=handler,
            Code=dict(ZipFile=zipped_code),
            Timeout=15,
            MemorySize=512
        )
        return response

    def update_lambda_function(self, function_name, zip_file):
        with open(zip_file, 'rb') as f:
            zipped_code = f.read()

        response = self.client.update_function_code(
            FunctionName=function_name,
            ZipFile=zipped_code
        )
        return response

    def invoke_lambda_function(self, function_name, payload={}):
        response = self.client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  # can be 'Event' for async
            Payload=json.dumps(payload)
        )
        return json.loads(response['Payload'].read())

    # Add other necessary methods as required

