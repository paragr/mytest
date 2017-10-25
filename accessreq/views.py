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
from pprint import pprint
from libs.usersearch import FindLDAPUser
from django.contrib.auth.models import Group, Permission, User
from datetime import date
# Create your views here.

class AccessRequestsList(ListView):
	
	context_object_name = 'access_requests'
	template_name = 'accessreq/accessrequests_list.html'
	
	def get_queryset(self):
		queryset = AccessRequests.objects.filter(status__in=['Pending','Approved']).filter(requested_by = self.request.user)
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
	
	def form_valid(self, form):
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
	

class ApproveRequest(AjaxableResponseMixin,FormView):
	model = AccessRequests
	
	def get(self, request, *args, **kwargs):
		id = kwargs['id']
		self.obj = self.model.objects.get(pk=id)
		result = self.adduser_group()
		self.obj.message = result
		self.obj.status = "Approved"
		self.obj.approved_by = request.user.username
		self.obj.approved_date = date.today()
		self.obj.save()

		if self.request.is_ajax():
			data = {
				'result': self.obj.pk,
			}
			return JsonResponse(data)
		else:
			return result

	def add_user(self,userdata):
		user,created = User.objects.get_or_create(username=userdata['username'])
		user.first_name = userdata['first_name']
		user.last_name = userdata['last_name']
		if userdata.has_key('email'):
			user.email = userdata['email']
		else:
			user.email = ""
		user.save()
		return user

	def add_group_member(self,user):
		group_name = self.obj.env
		new_group, created = Group.objects.get_or_create(name=group_name)
		if created:
			env_perm = Permission.objects.get(name='Stop Enviornment Services')
			new_group.permissions.add(env_perm)
			env_perm = Permission.objects.get(name='Start Enviornment Services')
			new_group.permissions.add(env_perm)
			env_perm = Permission.objects.get(name='View Enviornment Services')
			new_group.permissions.add(env_perm)
		new_group.user_set.add(user)


	def adduser_group(self):
		users = self.obj.users_list
		search_obj = FindLDAPUser()

		message = ""
		if users.find(","):
			users = users.split(",")
			for user in users:
				user_data = search_obj.get_user(user)
				if user_data:
					user = self.add_user(user_data)
					self.add_group_member(user)
				else:
					message = "User "+user+" is not found."
		else:
			user_data = search_obj.get_user(users)
			if user_data:
				user = self.add_user(user_data)
				self.add_group_member(user)
			else:
				message = "User " + users + " is not found."
		return message