from django.urls import path

from . import views

urlpatterns = [
    path('', views.UploadDocumentView.as_view(), name='index'),
]

app_name = 'ocr'
