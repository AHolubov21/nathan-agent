import json
import os
import requests
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import openai
import boto3
from datetime import datetime, timedelta
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация клиентов
slack_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
openai.api_key = os.environ['OPENAI_API_KEY']
dynamodb = boto3.resource('dynamodb', region_name=os.environ['DYNAMODB_REGION'])

# Таблицы DynamoDB
alerts_table = dynamodb.Table(os.environ['ALERTS_TABLE_NAME'])
runbooks_table = dynamodb.Table(os.environ['RUNBOOKS_TABLE_NAME'])
analytics_table = dynamodb.Table(os.environ['ANALYTICS_TABLE_NAME'])

# Функция для получения ранбука из GitLab
def get_runbook_from_gitlab():
    gitlab_token = os.environ['GITLAB_API_TOKEN']
    gitlab_project_id = os.environ['GITLAB_PROJECT_ID']
    gitlab_file_path = os.environ['GITLAB_FILE_PATH']
    headers = {'PRIVATE-TOKEN': gitlab_token}
    url = f"https://gitlab.com/api/v4/projects/{gitlab_project_id}/repository/files/{gitlab_file_path}/raw"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Это вызовет исключение для не 2xx ответов
        return response.text
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")  # HTTP error
    except Exception as err:
        logging.error(f"Other error occurred: {err}")  # Other errors

# Функция для анализа алерта с помощью OpenAI
def analyze_alert_with_openai(alert_message, runbook):
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Runbook:\n{runbook}\n\nAlert:\n{alert_message}\n\nPriority:",
            max_tokens=50
        )
        priority = response.choices[0].text.strip()
        action_required = "escalate" if "High" in priority or "Disaster" in priority else "acknowledge"
        return priority, action_required
    except openai.error.OpenAIError as e:
        logging.error(f"Error with OpenAI: {e}")

# Функция для ожидания резолва алерта
def wait_for_resolve(alert_id, alert_channel, timeout=600):
    start_time = datetime.now()
    while datetime.now() - start_time < timedelta(seconds=timeout):
        if check_for_resolve(alert_id):
            post_message(alert_channel, "Alert resolved within the expected time frame.")
            return True
        time.sleep(30)  # Проверяем каждые 30 секунд
    post_message(alert_channel, "Alert has not been resolved in the expected time frame, escalating.")
    return False

# Функция для проверки резолва алерта
def check_for_resolve(alert_id):
    try:
        messages = slack_client.conversations_history(channel=os.environ['ALERTS_CHANNEL_ID'])
        for message in messages['messages']:
            if f"resolved {alert_id}" in message['text']:
                return True
        return False
    except SlackApiError as e:
        logging.error(f"Error fetching messages: {e}")

# Функция для отправки сообщения в Slack
def post_message(channel, text):
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        logging.error(f"Error posting message: {e}")

# Функция для эскалации алерта
def escalate_alert(alert_message, alert_channel, priority):
    try:
        # ... (код остается прежним)
    except SlackApiError as e:
        logging.error(f"Error escalating alert: {e}")

# Функция для подтверждения алерта
def acknowledge_alert(alert_message, alert_channel):
    try:
        # ... (код остается прежним)
    except SlackApiError as e:
        logging.error(f"Error acknowledging alert: {e}")

# Основная функция Lambda
def lambda_handler(event, context):
    try:
        # ... (код остается прежним)
    except Exception as e:
        logging.error(f"Error in lambda_handler: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }
