from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/<int:catid>/', views.categ, name='cats')
]
