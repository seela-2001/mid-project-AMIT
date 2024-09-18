from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    reviews = models.IntegerField(default=0)
    category = models.CharField(max_length=100)

    class Meta:
        db_table = "products"

