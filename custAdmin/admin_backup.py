# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User,Group
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
			print "users groups are : ",request.user.groups
			perm_fields = ('is_active', 'is_staff', 'groups')

        return [(None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
                (_('Permissions'), {'fields': perm_fields}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')})]

		
admin.site.register(User, MyUserAdmin)