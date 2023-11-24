from django.urls import path
from .views import index, about, list_personagem, list_review


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('list/',list_personagem,name='list'),
    path('comentarios/<int:post_id>/', list_review, name='revi'),
]

