from django.urls import path

from . import views
app_name='blog'

urlpatterns=[

    path('signin/',views.signin,name='signin'),
    path('',views.profile, name='profile'),
    path('<str:username>',views.friendprofile,name='friendprofile'),
    path('addfriend/',views.addfriend, name='addfriend'),

    path('note/',views.note, name='note'),
    path('signin/',views.logout,name='logout'),



]