from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('reader', views.reader, name='reader'),
    path('readApi', views.readApi, name='readApi'),    
]