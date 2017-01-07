from django.db import models
import subprocess


# Create your models here.
class DockerFile(models.Model):
    repository = models.TextField(unique=True)
    file = models.FileField(upload_to='dockerfiles')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        subprocess.call(['scripts/build.sh', self.repository, self.file.path])







