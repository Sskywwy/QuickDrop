from django.urls import path
from . import views
from .views import  FileUploadView, FileListView, FileDownload
urlpatterns = [
    #path('upload/', views.FileUploadView.as_view(), name='upload'),
    path('file/<int:id>', views.FileRetrieveView.as_view(), name='file'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),  # Список всіх файлів
    #path('download/<str:filename>/', FileDownloadView.as_view(), name='file-download'),  # Завантаження за ID
    

]