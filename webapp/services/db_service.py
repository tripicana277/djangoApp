from webapp.models import UploadRecord

def save_to_db(filename, content):
    UploadRecord.objects.create(
        filename=filename,
        content=content
    )
