
from django.contrib import admin
from django.urls import path, include
from postApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postApp.urls')),
   
]

