#!python
# log/urls.py
from django.conf.urls import url
from . import views
from views import AccessRequestsList,RaiseRequest

app_name = 'accessreq'
# We are adding a URL called /home
urlpatterns = [
    url(r'^view_requests_list/$', AccessRequestsList.as_view(),name="list_access_req"),
	url(r'^raise_request/$', RaiseRequest.as_view(),name="raise_access_req"),
]