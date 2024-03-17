from django.db import models
from django.contrib.auth.models import User

class product_data(models.Model):
    pro_name=models.CharField(max_length=255,null=True)
    pro_price=models.FloatField(null=True)
    pro_description=models.CharField(max_length=300,null=True)
    XS=models.BooleanField(default=False)
    S=models.BooleanField(default=False)
    M=models.BooleanField(default=False)
    L=models.BooleanField(default=False)
    XL=models.BooleanField(default=False)
    pro_image=models.ImageField(upload_to='images/',blank=True)
    
    def __str__(self):
        return self.pro_name

class user_Model(models.Model):
    user_birth=models.DateField(null=True)
    user_address=models.CharField(max_length=255,null=True)
    user_number=models.IntegerField(null=True)
    user_gender=models.CharField(max_length=250,null=True)
    user_district=models.CharField(max_length=250,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class CartModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(product_data,through='cart_item')
    def total_price(self):
        cart_items = Cart_item.objects.filter(cart=self)
        total = sum(cart_item.subtotal() for cart_item in cart_items)
        return total
    
    
class Cart_item(models.Model):
    item = models.ForeignKey(product_data,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE)
    size = models.CharField(max_length=10,null=True)
    quantity = models.PositiveIntegerField(default=0)
    
    def subtotal(self):
        return self.item.pro_price * self.quantity
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    flat = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=20)
    town = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.fullname} - {self.town}, {self.state}'
# Create your models here.
