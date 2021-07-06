import json
import decimal
import os
import boto3

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return (str(obj))
        return super(DecimalEncoder, self).default(obj)

# Connect to the database

rdsData = boto3.client('rds-data')
parameters = boto3.client('ssm')

stage = os.environ['STAGE']
cluster_arn = os.environ['CLUSTERARN']
secret_arn = os.environ['SECRETARN']
dbname_param = parameters.get_parameter(Name='/school-vue-db-serverless/'+stage+'/database/name')


def lambda_handler(event, context):

    student_id = event['pathParameters']['student_id']
    sql = f'SELECT Math, Biology, Chemistry, Physics, Languages, Arts, Sports, Politics FROM grades WHERE Student_ID={student_id}'
        
    grades = rdsData.execute_statement(
            resourceArn = cluster_arn,
            secretArn = secret_arn,
            database = dbname_param['Parameter']['Value'],
            sql = sql)

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({
            "grades": grades['records']
        }, cls=DecimalEncoder)
    }
