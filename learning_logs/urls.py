"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #Page for displaying a list of topics
    path('topics/', views.topics, name='topics'),
    # Page for viewing posts on this topic
    path('topics/<topic_id>/', views.topic, name='topic'),
    # Page for adding a new theme
    path('new_topic/', views.new_topic, name='new_topic'),
    # new entry
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    # edit entry
    path('edit_entry/<entry_id>', views.edit_entry, name='edit_entry'),

]
