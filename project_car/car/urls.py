from django.urls import path
from . import views

urlpatterns = [
    path('', views.lists, name='lists'),
    path('delete', views.delete, name='delete'),
    path('add', views.add, name='add'),
]
