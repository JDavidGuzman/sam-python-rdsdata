# AWS API Gateway and AWS Lambda

This project was developed throug AWS Serverless Application Model, a Cloudformation extensions that makes easier to develop serverless infrastructures on AWS cloud. In this case, here is contained the code for three AWS Lambda functions using python 3.8 runtime, triggered by AWS API Gateway. These functions use Boto3; the python AWS SDK,  in order to access to AWS Parameter Store and AWS Secrets Manager for querying RDS through Data API.

## AWS Serverless Apolication Model 

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- get_schools, get_course, get_grades - Code for the application's Lambda functions, using python 3.8 runtime.
- events - Invocation events that you can use to invoke the function. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.
