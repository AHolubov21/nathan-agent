# audit_handler.py

import json
from audit_module import log_action, fetch_audit_logs

def lambda_handler(event, context):
    """
    AWS Lambda handler for audit functionalities.
    
    :param event: AWS Lambda uses this parameter to pass in event data to the handler.
    :param context: AWS Lambda uses this parameter to provide runtime information to your handler.
    
    :return: Response dictionary.
    """
    
    response = {
        'statusCode': 200,
        'body': '',
        'headers': {
            'Content-Type': 'application/json'
        }
    }
    
    try:
        # Check if it's a log action request or fetch logs request
        if event.get('action') == 'log':
            action_type = event.get('actionType')
            details = event.get('details')
            
            if not action_type or not details:
                raise ValueError("Missing required parameters for log action.")
            
            log_action(action_type, details)
            response['body'] = json.dumps({'message': 'Action logged successfully.'})
            
        elif event.get('action') == 'fetch':
            start_time = event.get('startTime')
            end_time = event.get('endTime')
            action_type = event.get('actionType')
            
            logs = fetch_audit_logs(start_time=start_time, end_time=end_time, action_type=action_type)
            response['body'] = json.dumps({'logs': logs})
            
        else:
            raise ValueError("Invalid action specified.")
            
    except Exception as e:
        response['statusCode'] = 400
        response['body'] = json.dumps({'error': str(e)})
        
    return response

