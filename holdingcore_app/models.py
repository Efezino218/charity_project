from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

import re

import requests 


# Create your models here.


class User(AbstractUser):
    # Add custom fields if needed
    pass


class Program(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)

    def get_youtube_embed_url(self):
        """Extract YouTube video ID and return embed URL if embeddable."""
        if not self.video_url:
            return None

        # Patterns for different YouTube URL formats
        patterns = [
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)',  # Regular YouTube URL
            r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]+)',               # Shortened YouTube URL
        ]

        for pattern in patterns:
            match = re.search(pattern, self.video_url)
            if match:
                video_id = match.group(1)

                # Check embeddability using YouTube's oEmbed API
                oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
                response = requests.get(oembed_url)

                if response.status_code == 200:
                    # The video is embeddable
                    return f"https://www.youtube.com/embed/{video_id}"
                else:
                    # The video is not embeddable
                    return None

        return None

    def clean(self):
        """Validate that only one media type is selected and YouTube URL is embeddable."""
        media_fields = [self.photo, self.video_url, self.video_file]
        filled_fields = [field for field in media_fields if field]

        if len(filled_fields) > 1:
            raise ValidationError("You can only select one media type: photo, video URL, or video file.")

        # Validate YouTube URL if provided
        if self.video_url and not self.get_youtube_embed_url():
            raise ValidationError("The provided YouTube video cannot be embedded. Please choose another video.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

