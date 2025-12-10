from django.urls import path
from .views import upload_view

# from django.shortcuts import redirect

urlpatterns = [
    path("upload/", upload_view, name="upload"),
    # path("", lambda request: redirect("upload"), name="root"),
]
