# Generated by Django 4.0.5 on 2022-06-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('email_phone', models.EmailField(max_length=254)),
            ],
        ),
    ]
