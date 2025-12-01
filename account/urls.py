from django.urls import path

from . import views



urlpatterns = [

    path('register', views.register, name='register'),

    # Login / Logout urls

    path('my-login', views.my_login, name='my-login'),

    path('user-logout', views.user_logout, name='user-logout'),

    # Manage shipping url

    path('manage-shipping/', views.manage_shipping, name='manage-shipping'),

    # Track orders url

    path('track-orders', views.track_orders, name='track-orders')

    

]