from django.urls import path, re_path
from . import views

#app_name = 'play'
app_name = 'reviews'
urlpatterns = [
    path('reviews/', views.write_review, name='write_review'),
    path('reviews/success', views.success, name='success'),
    ]
