import datetime
from db_models import FeedbackModel

class Feedback:
    def __init__(self, user_id, message, rating):
        """
        Инициализация объекта отзыва.

        :param user_id: ID пользователя.
        :param message: Сообщение отзыва.
        :param rating: Оценка от 1 до 5.
        """
        self.user_id = user_id
        self.message = message
        self.rating = rating
        self.timestamp = datetime.datetime.utcnow()

    def save_to_db(self):
        """
        Сохранение отзыва в базе данных.
        """
        feedback = FeedbackModel(
            feedback_id=str(self.timestamp),
            user_id=self.user_id,
            message=self.message,
            rating=self.rating,
            timestamp=self.timestamp
        )
        feedback.save()

def get_all_feedbacks():
    """
    Получение всех отзывов из базы данных.
    """
    return [feedback for feedback in FeedbackModel.scan()]

def get_feedback_by_user(user_id):
    """
    Получение всех отзывов конкретного пользователя.

    :param user_id: ID пользователя.
    """
    return [feedback for feedback in FeedbackModel.scan() if feedback.user_id == user_id]

def get_average_rating():
    """
    Расчет средней оценки из всех отзывов.
    """
    total_rating = 0
    feedback_count = 0
    for feedback in FeedbackModel.scan():
        total_rating += feedback.rating
        feedback_count += 1

    return total_rating / feedback_count if feedback_count else 0

# Пример использования:
# feedback = Feedback(user_id="12345", message="Great app!", rating=5)
# feedback.save_to_db()
# average_rating = get_average_rating()
