from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('',views.indexView, name='index'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='users/passwordChange.html'),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name='users/passwordChangeDone.html'),name='password_change_done'),
]