from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('all-games/', views.all_games, name='all_games'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    
    # GAMES
    path('all-games/yeezle/', views.yeezle, name='yeezle'),
]