# store/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', LoginView.as_view(template_name='store/login.html', next_page='/'), name='login'),
    path('games/<int:pk>/', views.game_detail, name='game_detail'),
    path('profile/', views.profile_view, name='profile'),
]