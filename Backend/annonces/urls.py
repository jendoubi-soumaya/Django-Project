from django.urls import path
from . import views

urlpatterns = [
    path('', views.annonce_list, name='annonce_list'),
    path('create/', views.create_annonce, name='create_annonce'),
    path('update/<int:pk>/', views.update_annonce, name='update_annonce'),
    path('delete/<int:pk>/', views.delete_annonce, name='delete_annonce'),
]
