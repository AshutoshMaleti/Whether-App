from django.db import models
from django.db.models.base import Model

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=25, verbose_name='city')

    class Meta:
        db_table = 'City'

    def __str__(self):
        return self.city