from PIL import Image
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Product(models.Model):
    image=models.ImageField(upload_to='images')
    image1=models.ImageField(upload_to='images',null=True,blank=True)
    image2=models.ImageField(upload_to='images',null=True,blank=True)
    
    title=models.CharField(max_length=250)
    rating=models.IntegerField(null=True,blank=True)
    description=RichTextField(null=True)
    price=models.IntegerField()
    discount=models.IntegerField()

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, blank=True)
    # quantity=models.IntegerField(default=0)

    def __str__(self):
        return "Cart of " + self.user.username
