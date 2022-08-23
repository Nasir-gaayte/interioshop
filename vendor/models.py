

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.OneToOneField(User,related_name='ven',on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name    