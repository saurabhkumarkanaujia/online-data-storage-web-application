# Generated by Django 3.1.7 on 2021-04-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0006_auto_20210429_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_model',
            name='file_name',
            field=models.TextField(null=True),
        ),
    ]