import unittest
from src.alerts.alerts_module import Alerts
from src.database.db_utils import Database  # Предположим, что у вас есть такой модуль

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        self.alerts = Alerts()
        self.database = Database()

    def test_alerts_database_integration(self):
        """
        Тест на корректность записи уведомления в базу данных и его последующего извлечения.
        """
        # Создаем уведомление
        self.alerts.trigger_alert("Integration test alert message")
        
        # Имитируем запись в базу данных
        self.database.store_alert("Integration test alert message")
        
        # Извлекаем уведомление из базы данных
        stored_alert = self.database.retrieve_alert()

        self.assertEqual(stored_alert, "Integration test alert message")

    # Добавьте другие интеграционные тесты...

if __name__ == '__main__':
    unittest.main()
