from django.contrib import messages
from django.shortcuts import redirect, render
from PIL import Image as PILimage
from django.contrib.auth import authenticate,login,logout

from clone.decorators import unauthenticated_user
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


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


@unauthenticated_user
def register(request):
    if request.method=='POST':
        email_phone=request.POST.get('email-phone')
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if password==password1:
            user,create=User.objects.get_or_create(username=username)
            if create:
                try:
                    validate_password(password)
                    user.set_password(password)
                    user.profile.fullname=fullname
                    user.profile.email_phone=email_phone
                    user.profile.save()
                    user.save()
                    messages.success(request,'Account created succesfully')
                    return redirect('login')
                except ValidationError as e:
                    messages.error(request,'Password error {e} ')
                    
            else:
                messages.info(request,'user with these details already exists')
        else:
            messages.error(request,'Passwords do not match')
    return render(request,'accounts/register.html')


@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        print('user',user)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'User with this credentials not found')

    return render(request,'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def editProfile(request):
    return render(request,'pages/editprofile.html')