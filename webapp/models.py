from django.db import models


class UploadRecord(models.Model):
    filename = models.CharField(max_length=255)
    content = models.TextField()  # 元テキスト保存
    xml_output = models.TextField(null=True, blank=True)  # XML保存用
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "upload_record"

    def __str__(self):
        return self.filename
