from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.loginView, name="login"),
    path('logout/', views.CustomLogoutView.as_view(),  name='logout'),
    path('',views.indexView, name='index'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='users/passwordChange.html'),name='password_change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name='users/passwordChangeDone.html'),name='password_change_done'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='users/passwordReset.html'), name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='users/passwordResetDone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/passwordResetConfirm.html'),name='password_reset_confirm'),
    path('reset/complete',auth_views.PasswordResetCompleteView.as_view(template_name='users/passwordResetComplete.html'),name='password_reset_complete'),
    path('register/',views.registerView, name='register'),
    path('edit/',views.editView,name='edit'),
    
]