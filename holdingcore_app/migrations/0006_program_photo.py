# Generated by Django 5.1.3 on 2025-01-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holdingcore_app', '0005_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
