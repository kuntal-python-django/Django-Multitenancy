from django.db import models
from tenant_schemas.models import TenantMixin


class User(models.Model):
    name = models.CharField(max_length=50, default='Kuntal Samanta', null=True, blank=True)
    username = models.CharField(max_length=10, default='kuntal', null=True, blank=True)
    
    def __str__(self):
        return self.name
