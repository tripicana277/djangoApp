from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadForm
from .models import UploadRecord
from .utils import parse_txt_to_rows, rows_to_xml


def upload_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            upload_file = request.FILES["file"]

            # TXT解析
            original_text, rows = parse_txt_to_rows(upload_file)

            # XML生成
            xml_str = rows_to_xml(rows)

            # DB保存
            record = UploadRecord.objects.create(
                filename=upload_file.name,
                content=original_text,
                xml_output=xml_str,
            )

            # XMLダウンロード
            response = HttpResponse(xml_str, content_type="application/xml")
            response["Content-Disposition"] = (
                f'attachment; filename="{record.filename}.xml"'
            )
            return response
    else:
        form = UploadForm()

    return render(request, "webapp/upload.html", {"form": form})
