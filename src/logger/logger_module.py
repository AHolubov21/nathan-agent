# logger_module.py

import boto3
import datetime

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'NathanLogger'
table = dynamodb.Table(table_name)

def log_event(event_type, message):
    """
    Log an event to DynamoDB.

    Args:
        event_type (str): Type of the event (e.g., 'INFO', 'ERROR', 'WARNING').
        message (str): Descriptive message associated with the event.

    Returns:
        dict: Response from DynamoDB.
    """
    timestamp = datetime.datetime.now().isoformat()
    
    log_item = {
        'event_type': event_type,
        'timestamp': timestamp,
        'message': message
    }
    
    response = table.put_item(Item=log_item)
    return response

def fetch_logs(event_type=None, start_time=None, end_time=None):
    """
    Fetch logs from DynamoDB based on provided filters.

    Args:
        event_type (str, optional): Filter logs by event type. Defaults to None.
        start_time (str, optional): Filter logs that occurred after this time. Defaults to None.
        end_time (str, optional): Filter logs that occurred before this time. Defaults to None.

    Returns:
        list[dict]: List of log items.
    """
    # Use scan for simplicity, but in a real-world scenario, consider using query for efficiency
    scan_filter = {}
    
    if event_type:
        scan_filter['event_type'] = {
            'AttributeValueList': [event_type],
            'ComparisonOperator': 'EQ'
        }
    
    if start_time:
        scan_filter['timestamp'] = {
            'AttributeValueList': [start_time],
            'ComparisonOperator': 'GE'
        }
    
    if end_time:
        if 'timestamp' in scan_filter:
            scan_filter['timestamp']['AttributeValueList'].append(end_time)
            scan_filter['timestamp']['ComparisonOperator'] = 'BETWEEN'
        else:
            scan_filter['timestamp'] = {
                'AttributeValueList': [end_time],
                'ComparisonOperator': 'LE'
            }

    response = table.scan(FilterExpression=scan_filter)
    return response['Items']

