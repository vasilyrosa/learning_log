"""Define padrões de URL para learning_logs."""
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #página inicial
    path('', views.index, name='index'),

    #Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),

    #Página de detalhes para um único assunto
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #página para adicionar um novo assunto
     path('new_topic/', views.new_topic, name='new_topic'),

     #página para adicionar uma nova entrada
     path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

     #página para editar uma entrada
     path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry')
]