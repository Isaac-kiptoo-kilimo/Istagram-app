from importlib.resources import contents
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    img_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',null=True)
    description=models.TextField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image_caption=models.CharField(max_length=200)
    size=models.CharField(max_length=50, null=True)
    profile=models.ForeignKey('Profile', on_delete = models.CASCADE)
    likes=models.IntegerField()
    comments=models.CharField(max_length=300)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.save_image
        self.delete()

    def update_caption(self,id,image_caption):
        updated_caption=Image.objects.filter(id=id).update(image_caption)
        return updated_caption

    def __str__(self):
        return self.img_name

class Profile(models.Model):
    name=models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='image/',null=True)
    bio=models.TextField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save_profile
        self.delete()

    def update_profile(self,id,profile):
        updated_profile=Profile.objects.filter(id=id).update(profile)
        return updated_profile
    def __str__(self):
        return self.name

class Comment(models.Model):
    title=models.CharField(max_length=100)
    comments=models.TextField()
    
    def __str__(self):
        return self.title

class Likes(models.Model):
    likes=models.CharField(max_length=100)

    def __str__(self):
        return self.likes