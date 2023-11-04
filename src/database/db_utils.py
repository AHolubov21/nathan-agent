import boto3

class DynamoDBUtils:
    def __init__(self, table_name, region_name='us-west-1'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.table = self.dynamodb.Table(table_name)

    def put_item(self, item):
        """
        Добавляет элемент в таблицу DynamoDB.

        :param item: Словарь с данными для добавления.
        """
        self.table.put_item(Item=item)

    def get_item(self, key):
        """
        Получает элемент из таблицы DynamoDB по ключу.

        :param key: Словарь с ключом для поиска элемента.
        :return: Элемент или None, если элемент не найден.
        """
        response = self.table.get_item(Key=key)
        return response.get('Item', None)

    def update_item(self, key, update_expression, expression_attribute_values):
        """
        Обновляет элемент в таблице DynamoDB.

        :param key: Словарь с ключом элемента для обновления.
        :param update_expression: Строка с выражением обновления.
        :param expression_attribute_values: Словарь с значениями для обновления.
        """
        self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values
        )

    def delete_item(self, key):
        """
        Удаляет элемент из таблицы DynamoDB.

        :param key: Словарь с ключом элемента для удаления.
        """
        self.table.delete_item(Key=key)

    def scan_table(self, filter_expression=None):
        """
        Производит сканирование таблицы DynamoDB.

        :param filter_expression: Опциональное выражение фильтрации.
        :return: Список элементов таблицы.
        """
        if filter_expression:
            response = self.table.scan(FilterExpression=filter_expression)
        else:
            response = self.table.scan()
        return response.get('Items', [])

# Пример использования:
# db = DynamoDBUtils('my-table-name')
# db.put_item({'id': '123', 'name': 'John', 'age': 30})
# item = db.get_item({'id': '123'})
# print(item)


# Additional utility functions for DynamoDB operations can be added here.

