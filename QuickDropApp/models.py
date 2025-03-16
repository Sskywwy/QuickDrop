from django.db import models

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    file = models.FileField(upload_to = 'uploads/')
    upload_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name if self.name else str(self.file) 