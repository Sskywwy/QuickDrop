from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.FileUploadView.as_view(), name='upload'),
    path('file/<int:id>', views.FileRetrieveView.as_view(), name='file'),
]