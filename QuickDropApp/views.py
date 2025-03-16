from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .models import File
from .serializers import FileSerializer
import os
from django.conf import settings
from rest_framework.exceptions import ValidationError
from django.http import Http404
def index(request):
    return render(request, 'index.html')

class FileUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileSerializer
    queryset = File.objects.all()
    def perform_create(self, serializer):
        file = serializer.validated_data.get('file')

        # Перевірка, чи файл вже був завантажений
        if File.objects.filter(name=file.name).exists():
            raise ValidationError("This file has already been uploaded.")

        # Якщо не існує, продовжуємо створення
        serializer.save()

class FileRetrieveView(generics.RetrieveAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    lookup_field = 'name'

class FileListView(generics.ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()

class FileDownloadView(generics.RetrieveAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'name'

    def get(self, request, filename, *args, **kwargs):
        # Пошук файлу по імені
        try:
            file = File.objects.get(name=filename)
            # Повертаємо файл у відповіді
            response = FileResponse(file.file)
            return response
        except File.DoesNotExist:
            # Якщо файл не знайдений, викидаємо помилку 404
            raise Http404("File not found")
# Create your views here.
