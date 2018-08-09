from django.urls import path

from . import views


app_name = 'smart'
urlpatterns = [
    path('', views.mic, name='mic'),
    path('', views.device, name='device'),
    path('', views.motion, name='motion'),
    path('', views.lights, name='lights'),
    path('', views.index, name='index'),
]
