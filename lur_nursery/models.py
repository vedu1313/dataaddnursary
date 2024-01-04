from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    cat_img = models.FileField(upload_to="media", blank=True, null=True)
    class Meta:
        db_table = "Category"
    def __str__(self):
      return self.name
class Sub_Category(models.Model):
    names = models.ForeignKey(Category, on_delete=models.CASCADE,default=0)
    subcat = models.CharField(max_length=50)
    sub_img = models.FileField(upload_to="media", blank=True, null=True)
    class Meta:
        db_table = "Sub_Category"
    def __str__(self):
      return self.subcat

class Sub_Categorys(models.Model):
    subcats = models.ForeignKey(Sub_Category, on_delete=models.CASCADE,default=0)
    sub    = models.CharField(max_length=50)
    class Meta:
        db_table = "Sub_Categorys"
    def __str__(self):
      return self.sub

class Items(models.Model):
    sub    = models.ForeignKey(Sub_Categorys, on_delete=models.CASCADE,default=0)
    name = models.CharField(max_length=50)
    dis_price = models.DecimalField(max_digits=10, decimal_places=3)
    org_price = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    item_img = models.FileField(upload_to="media", blank=True, null=True)
    conditions = models.CharField(max_length=50)
    offer =   models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=10, decimal_places=3,default=0)
    description = models.TextField(max_length=5000,default=0)
    class Meta:
        db_table = "Items"
    def __str__(self):
      return self.name