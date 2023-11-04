# orchestration_handler.py

import json
from orchestration_module import Orchestration

orchestration = Orchestration()

def handle_request(request):
    """
    Обрабатывает входящие запросы и передает их модулю оркестровки.
    """
    try:
        payload = json.loads(request.body)
        action = payload.get('action')
        
        if action == 'parse':
            data = payload.get('data')
            result = orchestration.orchestrate_parsing(data)
            return {
                'status': 'success',
                'data': result
            }

        elif action == 'handle_alerts':
            alert_type = payload.get('alert_type', "ALL")
            orchestration.handle_alerts(alert_type=alert_type)
            return {
                'status': 'success',
                'message': f'Handled alerts of type {alert_type}'
            }

        elif action == 'recovery':
            orchestration.orchestrate_recovery()
            return {
                'status': 'success',
                'message': 'Recovery process initiated'
            }

        else:
            return {
                'status': 'error',
                'message': f'Unsupported action: {action}'
            }

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

if __name__ == "__main__":
    # Пример входящего запроса
    request = {
        'body': json.dumps({
            'action': 'parse',
            'data': 'Some sample data for parsing'
        })
    }
    
    response = handle_request(request)
    print(response)
