# Generated by Django 3.1.7 on 2021-04-29 13:05

from django.db import migrations, models
import drive.models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0005_upload_model_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_model',
            name='uploaded_file',
            field=models.FileField(null=True, upload_to=drive.models.user_directory_path),
        ),
    ]
