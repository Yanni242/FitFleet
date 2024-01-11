from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import custom_logout

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'), 
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', custom_logout, name='logout'),
    path('bmi/', views.bmi, name = 'bmi'),
    path('calorie/', views.calorie, name = 'calorie'),
    path('weight/', views.weight, name = 'weight'),
    path('exercises/', views.exercises, name = 'exercises'),
]
