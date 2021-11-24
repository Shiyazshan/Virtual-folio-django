from django.db import models


class Service(models.Model):
    image = models.FileField(upload_to="service/")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    thumbnail = models.FileField()


