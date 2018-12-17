from django import forms
from .models import Image,Profile,Comments,Photolikes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CommentsForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.widget=forms.TextInput()
    class Meta:
        model = Comments
        fields = [ 'comment' ]


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')




class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','profile','comment']



# class likingphoto(Ajax):
#     def validate(self):
#         try:
#             self.postid = self.args[0]["id"]
#         except Exception as e:
#                 return self.error("Malformed request, did not process.")

#         if self.Image == "NL":
#             return self.error("Unauthorised request.")

#         if not Photolikes.objects.filter(liker=self.Image.name, postid=self.postid).exists():
#             Photo.objects.filter(id=self.postid).update(likes=F('likes')+1)
#             like = Photolikes(postid=self.postid, liker=self.Image.name)
#             like.save()
#         else:
#             photo.objects.filter(id=self.postid).update(likes=F('likes')-1)
#             Photolikes.objects.filter(poostid=self.postid, liker=self.Image.name).delete()


#         return self.success("Photo Liked")