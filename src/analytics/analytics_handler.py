# analytics_handler.py

from analytics_module import Analytics

def handle_request(request):
    """
    Обрабатывает входящий запрос к аналитическому модулю.
    """
    analytics = Analytics()

    if request["action"] == "generate_report":
        data = request.get("data", [])
        report = analytics.generate_report(data)
        return report

    elif request["action"] == "daily_trend_analysis":
        data = request.get("data", [])
        trends = analytics.daily_trend_analysis(data)
        return trends

    elif request["action"] == "monthly_performance":
        data = request.get("data", [])
        performance = analytics.monthly_performance(data)
        return performance

    else:
        return {"error": "Invalid action"}

def main():
    # Пример того, как может выглядеть входящий запрос
    sample_request = {
        "action": "generate_report",
        "data": [
            {"date": "2023-01-01", "value": 100},
            {"date": "2023-01-02", "value": 105},
            {"date": "2023-01-03", "value": 103},
            # ... и так далее
        ]
    }

    response = handle_request(sample_request)
    print(response)

if __name__ == "__main__":
    main()
