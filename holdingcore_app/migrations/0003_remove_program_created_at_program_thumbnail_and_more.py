# Generated by Django 5.1.3 on 2024-12-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holdingcore_app', '0002_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='created_at',
        ),
        migrations.AddField(
            model_name='program',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='program_thumbnails/'),
        ),
        migrations.AlterField(
            model_name='program',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='program',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='program_videos/'),
        ),
    ]
