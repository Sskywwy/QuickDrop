from django.shortcuts import render
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .models import File
from .serializers import FileSerializer
import os
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from rest_framework.exceptions import ValidationError
from django.http import Http404
from django.urls import reverse
from urllib.parse import unquote_plus


def index(request):
    return render(request, 'index.html')
@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(View):
    def post(self, request):
        uploaded_file = request.FILES.get('file')
        print (uploaded_file)
        
        file_instance = File.objects.create(
            file=uploaded_file,
            name=uploaded_file.name
        )
        filename = file_instance.file.name.split('/')[-1]
        

        download_url = ('http://localhost:4200'+ reverse('public-download', kwargs={
            'id': file_instance.id,
            'filename': filename
        }))
        download_url = unquote_plus(download_url)


        return JsonResponse({
            'message': 'Файл завантажено успішно',
            'download_url': download_url,
        })
    
class FileDownload(View):
    def get(self, request, id, filename):
        try:
            file = File.objects.get(id=id)
        except File.DoesNotExist:
            raise Http404("Файл не знайдено")
        # Формуємо шлях до файлу
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        print(file_path)
        # Перевіряємо чи файл існує
        if os.path.exists(file_path):
            print("Файл існує")
            # Якщо файл знайдений, відправляємо його як відповідь
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        else:
            # Якщо файл не знайдено, викидаємо помилку 404
            raise Http404("Файл не знайдено")
    



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
#Create your views here.
