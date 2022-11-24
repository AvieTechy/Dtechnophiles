from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include

from manager.views import (
    index, contract, worksheet, report, diary, project, plan, week1, week2, nhi, khoa, huyen, minh, loc, diary
)

urlpatterns = [
    path('', index, name="index"),
    path('contract/', contract, name="contract"),
    path('worksheet/', worksheet, name="worksheet"),
    path('report/', report, name="report"),
    path('diary/', diary, name="diary"),
    path('project/', project, name="project"),
    path('plan/', plan, name="plan"),
    path('week1/', week1, name="week1"),
    path('week2/', week2, name="week2"),
    path('nhi/', nhi, name="nhi"),
    path('khoa/', khoa, name="khoa"),
    path('minh/', minh, name="minh"),
    path('huyen/', huyen, name="huyen"),
    path('loc/', loc, name="loc"),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

