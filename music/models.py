from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

# class Album(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     release_date = models.DateField()

class Track(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    # album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/',validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    
    # release_date = models.DateField()

    def __str__(self):
        return f'{self.artist} - {self.title}'
    
    