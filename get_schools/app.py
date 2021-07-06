import json
import os
import boto3

# Connect to the database

rdsData = boto3.client('rds-data')
parameters = boto3.client('ssm')

stage = os.environ['STAGE']
cluster_arn = os.environ['CLUSTERARN']
secret_arn = os.environ['SECRETARN']
dbname_param = parameters.get_parameter(Name='/school-vue-db-serverless/'+stage+'/database/name')
schools = rdsData.execute_statement(
            resourceArn = cluster_arn,
            secretArn = secret_arn,
            database = dbname_param['Parameter']['Value'],
            sql = 'select * from schools')

def lambda_handler(event, context):
        
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({
            "schools": schools['records']
        })
    }
