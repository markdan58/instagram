from django.db import models

# Create your models here.  

class Profile(models.Model):
    username = models.CharField(max_length = 20)
    profileimage = models.ImageField(upload_to = "instagramprofile/")
    bio = models.CharField(max_length = 60)

    def __str__(self):
        return self.username


class Image(models.Model):
    name = models.CharField(max_length = 20)
    caption = models.CharField(max_length = 20)
    profile = models.ForeignKey(Profile)
    comments = models.TextField()
    photoimage = models.ImageField(upload_to ="instagramimages/")

    def __str__(self):
        return self.name 

class Comments(models.Model):
    username = models.CharField(max_length = 20)
    photoimage = models.ForeignKey(Image,related_name='Comments')
    comment = models.CharField(max_length = 60)
    profile = models.ForeignKey(Profile,related_name='Comments')

    def __str__(self):
        return self.username