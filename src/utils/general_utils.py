import os
import json
import datetime
import requests

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_to_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def current_timestamp():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def generate_unique_message(template, alert_name, priority=None):
    OPENAI_API_KEY = "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"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "prompt": f"Based on the template: '{template}', create a unique message for an alert named '{alert_name}' with priority '{priority}'",
        "max_tokens": 150
    }
    
    response = requests.post("https://api.openai.com/v1/engines/davinci/completions", headers=headers, data=json.dumps(data))
    message = response.json().get("choices", [{}])[0].get("text", "").strip()
    
    return message

