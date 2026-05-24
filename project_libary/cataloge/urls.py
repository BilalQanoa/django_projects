from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.Create.as_view(), name='create'),
    path('details/<int:pk>', views.Details.as_view(), name='details'),
    path('accounts/register/', views.Regiser.as_view(), name='register'),
    path('accounts/change-pass/', views.ChangePass.as_view(), name='change-pass'),

]
