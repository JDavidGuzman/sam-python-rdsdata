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

def lambda_handler(event, context):

    school_id = event['pathParameters']['school_id']
    course_id = event['pathParameters']['course_id']
    sql1 = f'SELECT Teacher_ID, Firstname, Lastname, Email FROM teachers WHERE School_ID={school_id} AND Level="{course_id}"'
    sql2 = f'SELECT Student_ID, Firstname, Lastname, Email FROM students WHERE School_ID={school_id} AND Level="{course_id}"'
    teacher = rdsData.execute_statement(
            resourceArn = cluster_arn,
            secretArn = secret_arn,
            database = dbname_param['Parameter']['Value'],
            sql = sql1)
    students = rdsData.execute_statement(
            resourceArn = cluster_arn,
            secretArn = secret_arn,
            database = dbname_param['Parameter']['Value'],
            sql = sql2)
        
    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({
            "teacher": teacher['records'],
            "students": students['records']
        })
    }
