from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute
from datetime import datetime

class UserModel(Model):
    """
    Модель пользователя в DynamoDB.
    """
    class Meta:
        table_name = "Users"
        region = "us-west-1"

    user_id = UnicodeAttribute(hash_key=True)
    username = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)
    age = NumberAttribute(null=True)
    created_at = UTCDateTimeAttribute(default=datetime.utcnow)

class EventLogModel(Model):
    """
    Модель лога событий в DynamoDB.
    """
    class Meta:
        table_name = "EventLogs"
        region = "us-west-1"

    event_id = UnicodeAttribute(hash_key=True)
    user_id = UnicodeAttribute(null=False)
    action = UnicodeAttribute(null=False)
    timestamp = UTCDateTimeAttribute(default=datetime.utcnow)

# Пример использования:
# user = UserModel(user_id="12345", username="JohnDoe", email="johndoe@example.com")
# user.save()

# event = EventLogModel(event_id="log_12345", user_id="12345", action="login")
# event.save()
