import boto3
import json
import os

def lambda_handler(event, context):
    test = event["methodArn"]
    path = test.split("/")
    file_list = os.listdir('src/')
    file = os.path.split(file_list)
    print(file)
    f = open("src/test.yaml", 'r')
    if path[1] == "v1":
        print(f.read())
    else:
        print("Access Denied on Path")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from test-Lambda!')
    }