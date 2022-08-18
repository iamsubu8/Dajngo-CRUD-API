from itertools import product
from django.db import models

# Create your models here.
class crud_models(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=30,blank=True)
    product_price=models.IntegerField()
    product_created_date=models.CharField(max_length=10,blank=True)

    class Meta:
        db_table='crud_table'