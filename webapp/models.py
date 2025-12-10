from django.db import models


class UploadRecord(models.Model):
    filename = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "upload_record"  # ← SQL操作しやすいテーブル名指定
