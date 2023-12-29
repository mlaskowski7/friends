from django.urls import path
from . import views

urlpatterns =[
    path('create/', views.postCreateView,name='postCreate'),
    path('feed/',views.feedView,name='feed'),
    path('like/',views.like_postView,name='like')

]