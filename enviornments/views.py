from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import time
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Enviornments

@login_required(login_url="login")

def index(request):
	enviornments = Enviornments.objects.all()
	return render(request,'enviornments/index.html',{'enviornments' : enviornments})
    
def installed_services(request,env,db):
    time.sleep(10)
    installed_services = ['DS_23FR2384hk_SUDEVDEr'+db,'eTKM_23FR2384hk_SUDEVDEr'+db,'TSRDEV_23FR2384hk_SUDEVDEr'+db]
    running_services = ['DS_23FR2384hk_SUDEVDEr'+db,'eTKM_23FR2384hk_SUDEVDEr'+db,'TSRDEV_23FR2384hk_SUDEVDEr'+db]
    template = loader.get_template('enviornments/installed_services.html')
    return HttpResponse(template.render({'env' : env,'db' : db,'installed_services' : installed_services, 'running_services' : running_services}, request))
    
def stop_service(request,env,db,service):
    time.sleep(10)
    installed_services = ['DS_23FR2384hk_SUDEVDEr'+db,'eTKM_23FR2384hk_SUDEVDEr'+db,'TSRDEV_23FR2384hk_SUDEVDEr'+db]
    running_services = ['DS_23FR2384hk_SUDEVDEr'+db,'eTKM_23FR2384hk_SUDEVDEr'+db,'TSRDEV_23FR2384hk_SUDEVDEr'+db]
    running_services.remove(service)
    template = loader.get_template('enviornments/installed_services.html')
    return HttpResponse(template.render({'env' : env,'db' : db,'installed_services' : installed_services, 'running_services' : running_services}, request))

def start_service(request,env,db,service):
    time.sleep(10)
    installed_services = ['DS_23FR2384hk_SUDEVDEr'+db,'eTKM_23FR2384hk_SUDEVDEr'+db,'TSRDEV_23FR2384hk_SUDEVDEr'+db]
    running_services = ['DS_23FR2384hk_SUDEVDEr'+db,'eTKM_23FR2384hk_SUDEVDEr'+db,'TSRDEV_23FR2384hk_SUDEVDEr'+db]
    if service not in running_services:
        running_services.append(service)
    template = loader.get_template('enviornments/installed_services.html')
    return HttpResponse(template.render({'env' : env,'db' : db,'installed_services' : installed_services, 'running_services' : running_services}, request))
       