# Setup Guide for Nathan

This guide provides step-by-step instructions on how to set up the `Nathan` project on your local development environment.

## Prerequisites

- Python 3.8 or newer
- AWS CLI (configured with appropriate permissions)
- An active AWS account
- DynamoDB table

## Installation

### 1. Clone the Repository

Start by cloning the `Nathan` repository to your local machine:

```bash
#git clone https://github.com/yourusername/nathan.git
#cd nathan

### 2. Set Up a Virtual Environment
##To avoid potential conflicts with other Python projects, it's advisable to create a virtual environment.

##```bash
#python -m venv venv
#source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

### 3. Install Required Packages
Install the necessary Python packages using the provided requirements.txt file:

pip install -r requirements.txt

### 4. Configure AWS Lambda Environment Variables
Modify the config/lambda_env_variables.yaml file to reflect your AWS configurations and other necessary environment variables.

### 5. Set Up DynamoDB
Ensure that you have a DynamoDB table set up as per the configurations specified in config/dynamodb_config.yaml.

### 6. Additional Configurations
Update config/slack_config.yaml for Slack integrations.
Update config/monitoring_systems.yaml for monitoring configurations.
Update config/openai_config.yaml if you're integrating with OpenAI.

Running Tests
Once you've set everything up, you can run the unit and integration tests to ensure that everything is working as expected:

python -m unittest tests/unit/*
python -m unittest tests/integration/*

Deployment
For deploying your Lambda functions and other AWS resources, use the provided deployment scripts in the scripts/ directory.

Documentation
For more in-depth documentation, refer to:

docs/usage.md: How to use the Nathan system.
docs/api_reference.md: API endpoint documentation and specifications.

Support
If you encounter any issues during the setup or have any questions regarding the project, please raise an issue on the GitHub repository or contact the maintainer directly.

