# ServerlessApp

Hello. You can find a simple serverless application and CI/CD infrastructure templates in this repository.

Lambda function can be triggered by uploading a .csv file into the S3 bucket which is named "bucket-csv". Function processes the .csv file and send it to DynamoDB.

You can see the infrastructure cloudformation templates into Templates folder. You need to create a stack for global.yaml first. It will create the necessary permission on AWS. infra.yaml will create a pipeline on AWS Codepipeline for the serverless app with AWS Codebuild.