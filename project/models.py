from django.db import models

# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    language=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='Project_images')
