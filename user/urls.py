from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('profile/<pk>/', views.profile_user, name='user-profile'),
    path('profile/', views.profile_update, name='user-profile-update'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),
         name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),
         name='user-logout'),
]
