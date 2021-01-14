from django.urls import path, re_path
from . import views
from plays.views import PlayDetailSlugView , ViewDetailDateView
#app_name = 'play'
urlpatterns = [
    path('plays/', views.play_list, name='play_list'),
    #re_path('plays/(?P<pk>\d+)/?$', views.play_detail, name='play_detail')
    re_path('plays/(?P<slug>[\w-]+)/?$', PlayDetailSlugView.as_view(), name='play_detail'),
    #re_path('plays/(?P<slug>[\w-]+)/?$', views.play_detail  , name='play_detail'),
    #re_path('plays/seat/(?P<pk>\d+)/?$', views.seating, name='booking'),
    re_path('plays/seat/(?P<pk>\d+)/?$',  ViewDetailDateView.as_view(), name='seating'),
    

]
