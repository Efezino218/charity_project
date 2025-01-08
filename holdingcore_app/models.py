from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # Add custom fields if needed
    pass



class Program(models.Model):
    title = models.CharField(max_length=100)  # Limit title to 100 characters
    location = models.CharField(max_length=255)
    content = models.TextField(max_length=500)  # Limit content to 500 characters
    video_url = models.URLField(blank=True, null=True)  # YouTube link
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # Local upload

    def __str__(self):
        return self.title
    
    
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

