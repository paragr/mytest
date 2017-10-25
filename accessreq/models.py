# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.core.urlresolvers import reverse
# Create your models here.

class AccessRequests(models.Model):
	users_list = models.CharField(max_length=1000,blank=False)
	env = models.CharField(max_length=100,blank=False)
	status = models.CharField(max_length=100,null=True)
	requested_by = models.CharField(max_length=100,null=True)
	request_date = models.DateField(auto_now_add=True,null=True)
	approved_by = models.CharField(max_length=100,null=True)
	approved_date = models.DateField(null=True)
	message = models.CharField(max_length=1000,null=True)
	
	class Meta:
		db_table = 'access_requests'
		permissions = (('can_raise_request','Can Raise Access Request'),
					   ('can_approve_request','Can Approve Access Request'),
					   ('can_reject_request','Can Reject Access Request'),
					  )
	def get_absolute_url(self):
		return reverse('raise_access_req')