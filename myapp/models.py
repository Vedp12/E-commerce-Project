from django.db import models

# Create your models here.
class Main_Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Sub_category(models.Model):
    Main_Category=models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.sub_name
    
class Product(models.Model):
    Sub_category=models.ForeignKey(Sub_category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="image",blank=True,null=True)
    product_price=models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name
    
