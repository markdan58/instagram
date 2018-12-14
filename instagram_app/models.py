from django.db import models







# Create your models here.  

class Profile(models.Model):
    photoimage = models.ImageField(upload_to ="instgram_appimages/")
    bio = models.CharField(max_length = 60)

    def __str__(self):
        return self.bio



class Image(models.Model):
    name = models.CharField(max_length = 20)
    caption = models.CharField(max_length = 20)
    profile = models.ForeignKey(Profile)
    comments = models.TextField()
    photoimage = models.ImageField(upload_to ="instagramimages/")

    def __str__(self):
        return self.name 
