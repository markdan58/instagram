from django.db import models







# Create your models here.  
class Image(models.Model):
    name = models.CharField(max_length = 20)
    caption = models.TextField()
    profile = models.ForeignKey(profile)
    comments = models.TextField()
    like = models.ForeignKey(Category)
    photo = models.ImageField(upload_to ="instagram_appimages/")

    def __str__(self):
        return self.name 


class profile(models.Model):
    photoimage = models.ImageField(upload_to ="galleryimages/")
    bio = models.CharField(max_length = 60)

    def __str__(self):
        return self.name 