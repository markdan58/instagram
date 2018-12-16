from django.test import TestCase
from .models import Profile,Image,Comments


# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.danmark= Image(name = 'danmark', profile ='DMM', caption ='Kenya',comments = 'awsome')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.danmark,Image))


    # Testing Save Method
    def test_save_method(self):
        self.danmark.save_photo()
        images= Image.objects.all()
        self.assertTrue(len(images) > 0)

    #Testing delete method
    def test_delete_method(self):
        self.danmark.save_photo()
        self.danmark.delete_photo()

    #Testing update
    def test_update_method(self):
        self.danmark.save_photo()
        new_caption = Image.objects.filter().update()
        photos = Image.objects.get()
        self.assertTrue(photos)