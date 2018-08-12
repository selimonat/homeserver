from django.urls import path

from . import views


app_name = 'smart'
urlpatterns = [
    path(''           , views.index,  name='index'),
    path('<slug:source>/', views.interface, name='interface')
]
