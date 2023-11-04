import boto3

class S3Module:
    def __init__(self, bucket_name, region_name='us-west-1'):
        self.s3_client = boto3.client('s3', region_name=region_name)
        self.bucket_name = bucket_name

    def upload_file(self, file_path, object_name=None):
        """Загружает файл в S3.

        :param file_path: Путь к файлу на локальной машине.
        :param object_name: Имя объекта в S3. Если не указано, будет использоваться имя файла.
        """
        if not object_name:
            object_name = file_path.split('/')[-1]
        
        self.s3_client.upload_file(file_path, self.bucket_name, object_name)

    def download_file(self, object_name, destination_path):
        """Скачивает файл из S3.

        :param object_name: Имя объекта в S3.
        :param destination_path: Путь для сохранения файла на локальной машине.
        """
        self.s3_client.download_file(self.bucket_name, object_name, destination_path)

    def list_files(self, prefix=''):
        """Получает список файлов в S3.

        :param prefix: Префикс для фильтрации списка файлов.
        :return: Список имен файлов.
        """
        response = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
        files = []
        if 'Contents' in response:
            for content in response['Contents']:
                files.append(content['Key'])
        return files

# Пример использования:
# s3 = S3Module('my-bucket-name', 'us-west-1')
# s3.upload_file('path/to/local/file.txt', 'remote_filename.txt')
# s3.download_file('remote_filename.txt', 'path/to/save/file.txt')
# files = s3.list_files()
# print(files)
