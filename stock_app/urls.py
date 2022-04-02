from django.urls import path
from stock_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.HomeViewClass.as_view(), name='home'),

    # path('gallery/', views.gallery, name='gallery'),
    path('gallery/', views.GalleryViewClass.as_view(), name='gallery'),

    # path('services/', views.services, name='services'),
    path('services/', views.ServicesViewClass.as_view(), name='services'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # path('detail/<int:id>/', views.detail, name='detail'),
    path('<int:pk>/detail/', views.DetailViewClass.as_view(), name='detail'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),

    # path('delete/<int:id>/', views.delete, name='delete'),
    path('<int:pk>/delete/', views.DeletePictureView.as_view(), name='delete'),

    path('like/<int:id>/', views.like_unlike_picture, name='like'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='stock_app/accounts/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='stock_app/accounts/password_email_sent.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='stock_app/accounts/password_reset_form.html'
    ), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='stock_app/accounts/password_reset_done.html'
    ), name='password_reset_complete'),

    path('add_picture/', views.CreatePicture.as_view(), name='add_picture'),

    # path('update_picture/<int:id>/', views.update_picture, name='update_picture'),
    path('update_picture/<int:pk>/', views.UpdatePictureView.as_view(), name='update_picture')

]
