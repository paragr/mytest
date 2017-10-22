from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from enviornments.models import Enviornments

@receiver(post_save,sender=Enviornments)
def create_env_group(sender,**kwargs):
	group_name = kwargs['instance'].Database
	new_group, created = Group.objects.get_or_create(name=group_name)
	env_perm = Permission.objects.get(name='Stop Enviornment Services')
	new_group.permissions.add(env_perm)
	env_perm = Permission.objects.get(name='Start Enviornment Services')
	new_group.permissions.add(env_perm)
	env_perm = Permission.objects.get(name='View Enviornment Services')
	new_group.permissions.add(env_perm)
	

@receiver(post_delete,sender=Enviornments)
def delete_env_group(sender,**kwargs):
	group_name = kwargs['instance'].Database
	Group.objects.filter(name=group_name).delete()

