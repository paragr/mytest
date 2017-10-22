from django.contrib import admin

# Register your models here.

from .models import Enviornments

class EnviornmentsAdmin(admin.ModelAdmin):
	list_display = ('Enviornment','Database')
	
admin.site.register(Enviornments,EnviornmentsAdmin)