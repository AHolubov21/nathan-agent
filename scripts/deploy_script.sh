#!/bin/bash

# Define AWS CLI profile name (change if necessary)
PROFILE="default"

# Define AWS region (change if necessary)
REGION="us-west-2"  # Updated to match your DynamoDB and Lambda configuration

# Name of the Lambda deployment package
PACKAGE_NAME="nathan_lambda_package.zip"

# Name of the Lambda function
LAMBDA_FUNCTION_NAME="slackEventHandler"  # Updated to match your serverless.yml configuration

# S3 bucket for Lambda deployment package
S3_BUCKET="nathan-lambda-deployment-bucket"  # Ensure this bucket exists in the us-west-2 region

# Create a deployment package
echo "Creating deployment package..."
zip -r $PACKAGE_NAME . -x "*.git*" "deploy_script.sh" "update_script.sh"

# Upload deployment package to S3
echo "Uploading deployment package to S3..."
aws s3 cp $PACKAGE_NAME s3://$S3_BUCKET/ --profile $PROFILE --region $REGION

# Create or update Lambda function
echo "Deploying Lambda function..."
aws lambda update-function-code --function-name $LAMBDA_FUNCTION_NAME --s3-bucket $S3_BUCKET --s3-key $PACKAGE_NAME --publish --profile $PROFILE --region $REGION

# Clean up
rm $PACKAGE_NAME

echo "Deployment completed."
