from . import views
from django.urls import path

urlpatterns = [
     path('side/', views.side, name='side'),
     path('register/', views.register, name='register'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]