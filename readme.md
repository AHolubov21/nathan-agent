# Nathan's Slack Bot for Alert Management

## Description

Nathan's Slack Bot is an automated alert management system integrated with Slack and OpenAI to analyze and respond to alerts in real-time. The bot leverages machine learning to determine the priority of alerts and appropriate actions based on a runbook sourced from GitLab.

## New Features

- Automatic updating of runbooks from GitLab.
- Enhanced logic for alert resolution waiting.
- Escalation of high and disaster priority alerts.
- Logging and exception handling for improved debugging and reliability.

## Requirements

- AWS CLI
- Python 3.9+
- Serverless Framework
- Access to AWS, GitLab, Slack, and OpenAI.

## Installation

1. Clone the repository:
git clone hhttps://github.com/AHolubov21/nathan-bot
cd nathan-slack-bot

2. Install dependencies:
pip install -r requirements.txt
npm install -g serverless


3. Configure environment variables in the `.env` file based on the template `config/lambda_env_variables.yaml`.

4. Deploy the application using the Serverless Framework:
serverless deploy


## Usage

- Send an alert to the designated Slack channel, and the bot will automatically process it based on the runbook.
- For high-priority alerts, the bot will wait for resolution within a specified timeframe before escalating.
- Disaster priority alerts will be escalated immediately.

## Configuration

- `serverless.yml` contains the configuration for AWS Lambda and related resources.
- The `config/` directory contains configuration files for GitLab, Slack, OpenAI, and DynamoDB.

## Updating

Use `deploy_script.sh` and `update_script.sh` for deploying and updating AWS Lambda functions.

## License

Specify the project's license here.

## Contact

Provide contact information for support and inquiries.

---

Documentation updated on: [Date of the last update].
