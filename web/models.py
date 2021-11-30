from django.db import models


class Testimonial(models.Model):
    message = models.TextField(default=0)
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE,blank=True,null=True)
 
 
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
