from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
    
    def create(self, validated_data):
        # Замість генерування унікального імені просто беремо оригінальне ім'я файлу
        original_name = validated_data['file'].name  # Отримуємо оригінальне ім'я файлу
        validated_data['name'] = original_name  # Присвоюємо ім'я без змін
        return super().create(validated_data)