# audit_module.py

import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')

AUDIT_TABLE_NAME = "NathanAuditLog"

def log_action(action_type, details):
    """
    Log an action to the audit table in DynamoDB.
    
    :param action_type: Type of the action, e.g., 'ALERT_TRIGGERED', 'DATA_PARSED', etc.
    :param details: A dictionary containing detailed information about the action.
    """
    
    table = dynamodb.Table(AUDIT_TABLE_NAME)
    
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    log_entry = {
        'timestamp': timestamp,
        'actionType': action_type,
        'details': details
    }
    
    table.put_item(Item=log_entry)

def fetch_audit_logs(start_time=None, end_time=None, action_type=None):
    """
    Fetch the audit logs based on provided filters.
    
    :param start_time: Optional start time to filter logs.
    :param end_time: Optional end time to filter logs.
    :param action_type: Optional action type to filter logs.
    
    :return: List of audit logs.
    """
    
    table = dynamodb.Table(AUDIT_TABLE_NAME)
    
    # Construct the query expression
    expression = []
    expression_values = {}
    
    if start_time:
        expression.append('timestamp >= :start_time')
        expression_values[':start_time'] = start_time
        
    if end_time:
        expression.append('timestamp <= :end_time')
        expression_values[':end_time'] = end_time
        
    if action_type:
        expression.append('actionType = :action_type')
        expression_values[':action_type'] = action_type
        
    response = table.scan(
        FilterExpression=' and '.join(expression),
        ExpressionAttributeValues=expression_values
    )
    
    return response['Items']

