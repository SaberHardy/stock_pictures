from django.urls import path

from stock_app import views

urlpatterns = [
    path('', views.home, name='home')
]