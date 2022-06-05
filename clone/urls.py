from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('addimage/',views.addimage,name='addimage'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('edit/',views.editProfile,name='edit'),
]