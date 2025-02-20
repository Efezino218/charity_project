# Generated by Django 5.1.3 on 2024-12-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holdingcore_app', '0003_remove_program_created_at_program_thumbnail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='program',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='program',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
