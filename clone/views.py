from django.contrib import messages
from django.shortcuts import redirect, render
from PIL import Image as PILimage
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from clone.decorators import unauthenticated_user
from .models import *
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q 
from django.views.generic import TemplateView, ListView


# Create your views here.
@login_required(login_url='login')
def index(request):
    image=Image.objects.all()
    users=User.objects.all()
    count=0
    c_users=[]
    for user in users:
        if user in request.user.profile.followers.all() or user in request.user.profile.following.all():
            pass
        else:
            if count <= 10:
                if user == request.user:
                    pass
                else:
                    c_users.append(user)
    return render(request,'pages/index.html',{'images':image,'users':c_users})


@login_required(login_url='login')
def addPost(request): 
    if request.method=='POST':
        image=request.FILES.get('photo')
        caption=request.POST.get('caption')
        img=Image(img_name=image.name,image=image,image_caption=caption,profile=request.user)
        img.save_image()
        return redirect('index')
        
    return render(request,'pages/addImage.html')


@login_required(login_url='login')
def profile(request):
    user=User.objects.all()
    # current_user=request.GET.get('user')
    # logged_in_user=request.user.username
    # user_followers=len(FollowersCount.objects.filter(user=current_user))
    # print("number",user_followers)
    # user_following=len(FollowersCount.objects.filter(follower=current_user))
    # print(user_following)
    return render(request,'pages/profile.html',{'user':user})


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


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def editProfile(request):

    return render(request,'pages/editprofile.html')


@login_required(login_url='login')
def addComment(request,image_id):
    if request.method=='POST':
        img=Image.objects.get(id=image_id)
        comment=request.POST.get('comment')
        com=Comment.objects.create(user=request.user,img=img,comment=comment)
        com.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def addremovelike(request,image_id):
    if request.method=='POST':
        img=Image.objects.get(id=image_id)
        if img.likes.contains(request.user):
            img.likes.remove(request.user)
        else:
            img.likes.add(request.user)
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def addremovefollow(request,user_id):
    if request.method=='POST':
        user=request.user
        new_follow=User.objects.get(id=user_id)
        if user.profile.following.contains(new_follow):
            user.profile.following.remove(new_follow)  
        else:
            user.profile.following.add(new_follow)
        if new_follow.profile.followers.contains(user):
            new_follow.profile.followers.remove(user)
        else:
            new_follow.profile.followers.add(user)
    return redirect(request.META['HTTP_REFERER'])


class SearchResultsView(ListView):
    model = User
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = User.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list