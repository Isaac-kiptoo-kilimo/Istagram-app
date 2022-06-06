from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('addpost/',views.addPost,name='addpost'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('edit/',views.editProfile,name='edit'),
    path('addcomment/<str:image_id>/',views.addComment,name='addcomment'),
    path('addremovelike/<str:image_id>/',views.addremovelike,name='addremovelike'),
    path('addremovefollow/<str:user_id>/',views.addremovefollow,name='addremovefollow'),
   
]