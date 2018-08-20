from django.urls import path

from . import views


app_name = 'smart'
urlpatterns = [
    path(''           , views.index,  name='index'),
    path('test/', views.test, name='test'),
    path('<slug:source>/', views.interface, name='interface')
]
