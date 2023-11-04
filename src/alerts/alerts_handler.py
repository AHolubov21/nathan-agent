from alerts_module import AlertsModule

def handle_alert_event(event):
    alerts = AlertsModule()
    
    # Извлекаем информацию из события (event) и готовим сообщение для Slack.
    message = json.loads(event)['message']
    
    # Отправляем оповещение в Slack.
    alerts.send_alert(message)

    # Дополнительная логика обработки события.