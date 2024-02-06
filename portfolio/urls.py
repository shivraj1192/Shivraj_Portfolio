from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home , name='home'),
    # path('about', views.about , name='about'),
    # # path('resume', views.resume , name='resume'),
    path('contact/', views.contact , name='contact'),
    path('internship', views.internship , name='internship'),
    path('qrcode', views.qrcode , name='qrcode'),
    path('send', views.qrcode),
    path('remove_qrcode', views.remove_qrcode, name='remove_qrcode'),
    path('weather/', views.weather, name='weather'),
    path('download_qrcode/', download_qrcode, name='download_qrcode'),

    # path('blog', views.handleblogs , name='handleblogs'),

   
]