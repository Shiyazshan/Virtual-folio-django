from django.db import models


class Service(models.Model):
    image = models.ImageField(upload_to="service/")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
        

class Project(models.Model):
    thumbnail = models.ImageField(upload_to="projects/thumbnails/", blank=True, null=True)
    feature_image = models.ImageField(upload_to="projects/feature_image/", blank=True, null=True)
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    is_satisfied = models.BooleanField(default=False)
    clients = models.ForeignKey("users.Client",on_delete = models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name