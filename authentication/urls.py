from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    path('signout',views.signout, name="signout"),
    path('aboutus',views.aboutus, name="aboutus"),
    path('std10',views.std10, name="std10"),
    path('std11',views.std11, name="std11"),
    path('std12',views.std12, name="std12"),
    path('Btech',views.Btech, name="Btech"),
    path('it',views.it, name="it"),
    path('sem1it',views.sem1it, name="sem1it"),
    path('sem2it',views.sem2it, name="sem2it"),
    path('sem3it',views.sem3it, name="sem3it"),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin, name="signin"),
]