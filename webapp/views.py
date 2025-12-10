from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadForm
from .services.txt_parser import parse_text
from .services.xml_writer import generate_xml
from .services.db_service import save_to_db
from .services.db_service import save_to_db_sql


def upload_view(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES["file"]
            raw_text = uploaded_file.read().decode("utf-8")

            # DB 保存
            # save_to_db_sql(uploaded_file.name, raw_text)
            save_to_db(uploaded_file.name, raw_text)

            # テキスト解析
            parsed = parse_text(raw_text)

            # XML 生成
            xml_data = generate_xml(parsed)

            # XML ダウンロード応答
            response = HttpResponse(xml_data, content_type="application/xml")
            response["Content-Disposition"] = (
                f'attachment; filename="{uploaded_file.name}.xml"'
            )
            return response
    else:
        form = UploadForm()

    return render(request, "upload.html", {"form": form})
