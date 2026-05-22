from django.urls import path
from . import views

urlpatterns = [
    path('', views.Lists.as_view(), name='lists'),
    path('delete', views.Delete.as_view(), name='delete'),
    path('add', views.Add.as_view(), name='add'),
]
