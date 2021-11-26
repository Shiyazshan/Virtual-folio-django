from django.db import models


PROFILE_GENDER = (
    ("male","Male"),
    ("female","Female"),
    ("other","Other")
)


class Profile(models.Model):
    user_id = models.AutoField(unique=True, primary_key=True)
    image = models.ImageField(upload_to="profile/")
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    address = models.ForeignKey("users.Address",on_delete = models.CASCADE,blank=True,null=True)
    description = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=255, choices=PROFILE_GENDER)
    resume = models.FileField(upload_to="profile/")

    def __str__(self):
        return self.name


class Address(models.Model):
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)


class Education(models.Model):
    year = models.IntegerField()
    course = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    description = models.TextField()


class Experience(models.Model):
    year = models.IntegerField()
    course = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    description = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey("users.Profile",on_delete = models.CASCADE,blank=True,null=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Clients(models.Model):
    name =  models.CharField(max_length=255)
    image = models.FileField(upload_to="service/")
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.name