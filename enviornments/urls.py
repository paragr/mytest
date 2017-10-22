from django.conf.urls import url

from . import views

app_name = 'environments'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<env>\w+)/(?P<db>\w+)/inst/$', views.installed_services, name='installed_services'),
    url(r'^(?P<env>\w+)/(?P<db>\w+)/(?P<service>\w+)/stop/$', views.stop_service, name='stop_service'),
    url(r'^(?P<env>\w+)/(?P<db>\w+)/(?P<service>\w+)/start/$', views.start_service, name='start_service'),
]