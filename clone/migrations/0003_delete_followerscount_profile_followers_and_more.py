# Generated by Django 4.0.5 on 2022-06-06 11:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clone', '0002_alter_profile_profile_img'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FollowersCount',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]