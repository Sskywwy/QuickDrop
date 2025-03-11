from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import generics
from .models import File
from .serializers import FileSerializer
def index(request):
    return render(request, 'index.html')

class FileUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileSerializer
    queryset = File.objects.all()

class FileRetrieveView(generics.RetrieveAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    lookup_field = 'id'
# Create your views here.
