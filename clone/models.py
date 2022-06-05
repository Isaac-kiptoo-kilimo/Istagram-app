
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Image(models.Model):
    img_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/',null=True)
    image_caption=models.CharField(max_length=200)
    profile=models.ForeignKey(User, on_delete = models.CASCADE)
    likes=models.ManyToManyField(User,related_name='likes')
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self,id,image_caption):
        updated_caption=Image.objects.filter(id=id).update(image_caption)
        return updated_caption

    def __str__(self):
        return self.img_name


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullname=models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='image/',null=True)
    bio=models.TextField()
    email_phone=models.CharField(max_length=100)

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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            instance.profile.save()

        post_save.connect(Profile, sender=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ForeignKey(Image,on_delete=models.CASCADE)
    comment=models.TextField()
    
    def __str__(self):
        return self.comment

