from django.db import models


# Create your models here.
class DockerFile(models.Model):
    repository = models.TextField()
