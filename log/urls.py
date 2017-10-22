#!python
# log/urls.py
from django.conf.urls import url
from . import views

app_name = 'log'
# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
]