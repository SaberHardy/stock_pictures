from django.urls import path
from stock_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:id>/', views.detail, name='detail'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]
