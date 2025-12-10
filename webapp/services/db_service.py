from webapp.models import UploadRecord
from django.db import connection


def save_to_db(filename, content):
    UploadRecord.objects.create(filename=filename, content=content)


def save_to_db_sql(filename, content):
    sql = """
        INSERT INTO upload_record (filename, content, created_at)
        VALUES (%s, %s, CURRENT_TIMESTAMP)
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [filename, content])
