from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    category = models.ForeignKey(Category , on_delete= models.CASCADE,default=1)
    description = models.CharField(max_length=200,default=0,null=True,blank=True)
    image = models.ImageField(upload_to="uploads/products/")

    @staticmethod
    def get_all_proucts():
        return Product.objects.all()

    @staticmethod
    def get_all_proucts_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_proucts()