from django.db import models

class Product(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=60)
    product_category = models.CharField(max_length=60)
    product_price = models.FloatField()
    product_expiry_date = models.DateField()
    product_manufacturing_date = models.DateField()
    product_HSN_no = models.CharField(max_length=8)
    product_quantity = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['product_category']