# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import AccessRequests

# Register your models here.
class AccessRequestsAdmin(admin.ModelAdmin):
	list_display = ('users_list','env','status','requested_by','request_date','approved_by','approved_date')
	
	def get_fieldsets(self, request, obj=None):
		perm_fields = ('users_list', 'env')
			
		return [(None, {'fields': perm_fields})]
	
	def save_model(self,request,obj,form,change):
		obj.requested_by = request.user
		obj.status = "Pending"
		obj.save()

admin.site.register(AccessRequests,AccessRequestsAdmin)