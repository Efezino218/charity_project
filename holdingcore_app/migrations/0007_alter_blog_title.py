# Generated by Django 5.1.3 on 2025-01-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holdingcore_app', '0006_program_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
