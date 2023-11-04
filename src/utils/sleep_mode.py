import datetime

class SleepMode:
    def __init__(self):
        self.is_active = False
        self.start_time = None
        self.duration = None

    def activate(self, duration_in_hours=1):
        """
        Активация режима сна на заданное количество часов.

        :param duration_in_hours: Продолжительность режима сна в часах.
        """
        self.is_active = True
        self.start_time = datetime.datetime.utcnow()
        self.duration = datetime.timedelta(hours=duration_in_hours)

    def deactivate(self):
        """
        Деактивация режима сна.
        """
        self.is_active = False
        self.start_time = None
        self.duration = None

    def is_sleep_mode_active(self):
        """
        Проверка, активен ли режим сна.

        :return: True, если режим сна активен, иначе False.
        """
        if not self.is_active:
            return False
        if datetime.datetime.utcnow() - self.start_time > self.duration:
            self.deactivate()
            return False
        return True

# Пример использования:
# sleep_mode = SleepMode()
# sleep_mode.activate(duration_in_hours=2)
# print(sleep_mode.is_sleep_mode_active())  # Выведет True, если прошло менее 2 часов с момента активации
