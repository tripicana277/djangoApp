import pytest
from django.urls import reverse
from webapp.models import UploadRecord


# ① pytest 基本テスト (/upload 読み込み)
@pytest.mark.django_db
def test_upload_page_loads(client):
    url = reverse("upload")
    response = client.get(url)
    assert response.status_code == 200


# ② ファイルアップロードテスト
@pytest.mark.django_db
def test_file_upload(client):
    url = reverse("upload")
    file_data = {"upload_file": ("test.txt", b"Hello", "text/plain")}
    response = client.post(url, file_data)
    assert response.status_code == 200


# ③ DB保存が確認できるテスト
@pytest.mark.django_db
def test_db_entry_created(client):
    url = reverse("upload")

    client.post(url, {"file": ("dbtest.txt", b"Test DB!", "text/plain")})

    assert UploadRecord.objects.count() == 1


# ④ 認証が必要なページテスト例
def test_redirect_if_not_logged_in(client):
    response = client.get("/admin/")
    assert response.status_code in (302, 301)


# ⑤ API レスポンス(JSON)テスト(必要なら)
def test_json_api(client):
    response = client.get("/api/status/")
    assert response.json()["status"] == "ok"


# ⑥ pytest.ini を作成（重要）
# ⑦ GitHub Actionsで自動テスト（CI）


# ⑧ Azure WebApp に自動デプロイ（CD）
