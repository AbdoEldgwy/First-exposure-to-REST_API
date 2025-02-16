from django.db import models

# Create your models here.
class Product(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=120)
  content = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, default=99.99)
  