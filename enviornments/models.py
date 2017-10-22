from django.db import models
# Create your models here.

class Enviornments(models.Model):
    
    Enviornment = models.CharField(max_length=50)
    Database = models.CharField(max_length=50)
    
    class Meta:
        db_table = "enviornments"
        permissions = (("can_stop_services" , "Stop Enviornment Services"),
					   ("can_start_services" , "Start Enviornment Services"),
					   ("can_view_services" , "View Enviornment Services"),
					  )
	