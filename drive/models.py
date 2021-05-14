from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    return 'Users/user_{0}/{1}'.format(instance.owner.id, filename)

class Upload_model(models.Model):
    uploaded_file=models.FileField(upload_to=user_directory_path, null=True)
    file_name=models.CharField(max_length=245, null=True)
    file_size=models.CharField(max_length=245, null=True)
    file_type=models.CharField(max_length=245, null=True)
    user_name=models.CharField(max_length=100, null=True)