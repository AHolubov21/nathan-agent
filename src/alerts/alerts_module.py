from general_utils import generate_unique_message

class AlertsModule:

    def __init__(self, runbook_data, slack_module):
        self.runbook = runbook_data
        self.slack = slack_module

    def process_alert(self, alert):
        # Предполагая, что алерт приходит в формате JSON:
        alert_name = alert.get('alert_name')
        priority = self.runbook.get(alert_name)

        if not priority:
            return

        message = generate_unique_message("Alert received: {alert_name} with priority {priority}.", alert_name, priority)
        self.slack.send_message("#your_channel_name", message)
