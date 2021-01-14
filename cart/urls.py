from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.cart_home, name='home'),
    path('update/', views.cart_update, name='update'),
    path('updatea/', views.cart_update_again, name='updatea'),

]
