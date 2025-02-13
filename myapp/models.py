from django.db import models

class Main_Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Sub_category(models.Model):
    Main_Category=models.ForeignKey(Main_Category,on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.sub_name
    
class Size_filter(models.Model):
    size=models.CharField(max_length=100)
    
    def __str__(self):
        return self.size 
    
class Brand_filter(models.Model):
    brand=models.CharField(max_length=100)
    
    def __str__(self):
        return self.brand


class Product(models.Model):
    Sub_category=models.ForeignKey(Sub_category,on_delete=models.CASCADE)
    Size_filter=models.ForeignKey(Size_filter,on_delete=models.CASCADE,blank=True,null=True)
    Brand_filter=models.ForeignKey(Brand_filter,on_delete=models.CASCADE,blank=True,null=True)
    product_name=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to="image",blank=True,null=True)
    product_price=models.IntegerField()
    
    def __str__(self):
        return self.product_name