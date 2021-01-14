from django.urls import path, re_path
from . import views

app_name = 'visacheck'
urlpatterns = [
    path('visacheck/', views.visacheck, name='visacheck'),
    path('visacheck/success', views.success, name='success'),


]
