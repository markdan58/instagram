from django.db import models
from django.contrib.auth.models import User

# Create your models here.  

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
    profileimage = models.ImageField(upload_to = "instagramprofile/")
    bio = models.CharField(max_length = 60)

    @classmethod
    def search_profile(cls, name):
        profiles = Profile.objects.filter(user__username__icontains=name)
        return profiles


    def __str__(self):
        return self.user.username


class Image(models.Model):
    name = models.CharField(max_length = 20)
    caption = models.CharField(max_length = 20)
    profile = models.ForeignKey(Profile)
    comment = models.TextField()
    photoimage = models.ImageField(upload_to ="instagramimages/")
    likes = models.IntegerField()
   
    # @classmethod
    # def search_profile(cls, search_term):
    #     profiles = cls.objects.filter(profile__icontains=search_term)
    #     return profiles

    def __str__(self):
        return self.name 

    def save_Image(self):
        self.save()

class Comments(models.Model):
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="image_comments")
    comment = models.CharField(max_length = 60)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Photolikes(models.Model):
    postid = models.IntegerField()
    liker = models.CharField(max_length = 20)