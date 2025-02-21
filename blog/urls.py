from django.urls import path
from blog import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='home'),
]