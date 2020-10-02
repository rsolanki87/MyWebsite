from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    #Main page
    path('', views.portfolio, name='portfolio'),
]