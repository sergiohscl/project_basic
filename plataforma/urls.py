from django.urls import path
from plataforma import views


urlpatterns = [
    path('home/', views.home, name='home'),    
]
