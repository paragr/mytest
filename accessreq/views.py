# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from models import AccessRequests
from django.db.models import Q
from forms import AccessRequestForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.http import JsonResponse
# Create your views here.

class AccessRequestsList(ListView):
	
	context_object_name = 'access_requests'
	template_name = 'accessreq/accessrequests_list.html'
	
	def get_queryset(self):
		queryset = AccessRequests.objects.filter(Q(status = 'Pending') & Q(requested_by = self.request.user))
		return queryset

class AjaxableResponseMixin(object):
	
	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)
		else:
			return response
			
	def form_valid(self, form):
		# We make sure to call the parent's form_valid() method because
		# it might do some processing (in the case of CreateView, it will
		# call form.save() for example).
		self.obj = form.save(commit=False)
		self.obj.requested_by = self.request.user
		self.obj.status = "Pending"
		self.obj.save()
		
		response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax():
			data = {
				'pk': self.obj.pk,
			}
			return JsonResponse(data)
		else:
			return response
			
			

class RaiseRequest(AjaxableResponseMixin,FormView):
	template_name = 'accessreq/accessrequests_form.html'
	form_class = AccessRequestForm
	success_url = '/accessreq/view_requests_list/'
	model = AccessRequests

'''	
	def get(self, request, *args, **kwargs):
		print "*********************** inside get method ********************************"
		form = self.form_class()
		return render(request,self.template_name,{'form': form})
	
	def post(self, request, *args, **kwargs):
		print "*********************** inside post method ********************************"
		form = AccessRequestForm(request.POST)
		
		if form.is_valid():
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
			print "inside form valid case"
			self.obj = form.save(commit=False)
			self.obj.requested_by = request.user
			self.obj.status = "Pending"
			self.obj.save()
		
			return HttpResponseRedirect(self.success_url)
	
		return render(request,self.template_name,{'form': form})
'''