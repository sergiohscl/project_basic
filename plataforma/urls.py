from django.urls import path
from plataforma import views
from .api.viewsets import LivrosApiView, LivrosViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('livro', LivrosViewSet)

urlpatterns = [
    path('home/', views.home, name='home'),
    path('livros/', LivrosApiView.as_view(), name='livros'),
]
