# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _
admin.site.unregister(User)

class MyUserAdmin(UserAdmin):

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 'is_superuser',
								'groups', 'user_permissions')
        else:
            # modify these to suit the fields you want your
            # staff user to be able to edit
            perm_fields = ('is_active', 'is_staff','groups')
			
        return [(None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': perm_fields}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')})]

    def get_form(self, request, obj=None, **kwargs):
		form = super(MyUserAdmin, self).get_form(request, obj, **kwargs)
		
		if not request.user.is_superuser:
			if 'groups' in form.base_fields:
				mygroups = form.base_fields['groups']
				mygroups.queryset = mygroups.queryset.exclude(name='admins_group')
		return form
	
    def get_queryset(self, request):
		qs = super(MyUserAdmin, self).get_queryset(request)
		
		if not request.user.is_superuser:
			return qs.filter(is_superuser=False)
		return qs
		

admin.site.register(User, MyUserAdmin)