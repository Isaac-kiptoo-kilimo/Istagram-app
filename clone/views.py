from django.shortcuts import render
from PIL import Image as PILimage

from .forms import createUserForm
from .models import *


# Create your views here.

def index(request):
    image=Image.objects.all()
    return render(request,'pages/index.html',{'images':image})

def addimage(request):
    
    if request.method=='POST':
        image=request.FILES.get('photo')
        image_=PILimage.open(image)
        name=request.POST.get('name')
        size=f'{image_.width} x {image_.height}'
        description=request.POST.get('description')
        comments=request.POST.get('comment')
        comment_=Comment.objects.get(id=comments)
        likes=request.POST.get('location')
        likes_=Likes.objects.get(id=likes)
        img=Image(name=name,image=image,description=description,size=size,likes=likes_,comments=comment_)
        img.save_image()
    return render(request,'pages/addImage.html')

def profile(request):
    return render(request,'pages/profile.html')

def register(request):
    form=createUserForm()
    if request.method=='POST':
        form=createUserForm(request.POST)
        form.save()

    return render(request,'accounts/register.html')

def loginPage(request):
    form=createUserForm()
    if request.method=='POST':
        form=createUserForm(request.POST)
        form.save()

    return render(request,'accounts/login.html')