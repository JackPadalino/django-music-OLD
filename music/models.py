from django.db import models
from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import post_delete
import datetime
from django.utils import timezone
import os

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name='tracks')
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/',validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    upload_date = models.DateTimeField("date uploaded",default=timezone.now())

    def __str__(self):
        return f'{self.artist} - {self.title}'

# signal to handle file path deletion upon instance deletion
@receiver(post_delete, sender=Track)
def delete_file_on_track_delete(sender, instance, **kwargs):
    file_path = instance.file.path
    if os.path.exists(file_path):
        os.remove(file_path)