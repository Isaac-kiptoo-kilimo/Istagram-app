from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    img_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_caption=models.CharField(max_length=200)
    profile=models.ForeignKey('Profile', on_delete = models.CASCADE)
    likes=models.CharField(max_length=100)
    comments=models.CharField(max_length=300)


    def __str__(self):
        return self.img_name

class Profile(models.Model):
    name=models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='image/',null=True)
    bio=models.TextField()

    def __str__(self):
        return self.name



