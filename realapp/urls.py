from django.urls import path,include
from django.contrib import admin
from realapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("proper/",views.proper,name="proper"),
    path("search/",views.searchproperty,name="search"),
    path("proper/<str:slug>",views.property_detail,name="property_detail"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

