from django.db import models

class ProductCategory(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='product category')

    def __str__(self):
        return self.title

class ProductList(models.Model):
    category = models.ForeignKey(ProductCategory, default=1)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='product detail')
    price = models.DecimalField(decimal_places=2, max_digits=10, default=40.00)
    description = models.TextField()
    stock = models.IntegerField(default=30)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    offers = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

