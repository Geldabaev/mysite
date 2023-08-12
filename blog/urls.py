from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<int:catid>/', views.categ, name='cats'),
    path('post/<int:pk>/', views.detail, name='detail'),
]
