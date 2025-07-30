from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# video number 35 model create karva mate
class homepro(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(default='defult.png')
    price=models.IntegerField(default=0)
    descriptions=models.CharField(max_length=500,null=True)


class mens(models.Model):
    mname=models.CharField(max_length=100)
    mimage=models.ImageField(default='defult.png')
    mprice=models.IntegerField(default=0)
    mdescriptions=models.CharField(max_length=500,null=True)

class womens(models.Model):
    wname=models.CharField(max_length=100)
    wimage=models.ImageField(default='defult.png')
    wprice=models.IntegerField(default=0)
    wdescriptions=models.CharField(max_length=500,null=True)

# 
class Cart(models.Model):
    name=models.CharField(max_length=180,default='unnamed')
    desc=models.CharField(max_length=500,default=None)
    price=models.IntegerField(default=0)
    q=models.PositiveIntegerField(default=0)
    total_p=models.PositiveIntegerField(default=0)
    image=models.ImageField(default='defult.png')
    user=models.ForeignKey(User,on_delete=models.CASCADE)



class Checkout(models.Model):
    fullname=models.CharField(max_length=100)
    address=models.TextField()
    phonenumber=models.CharField(max_length=10)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=6)
    card_num=models.IntegerField(max_length=16)
    e_date=models.CharField(max_length=4)
    cvv=models.IntegerField(max_length=3)
    host=models.ForeignKey(User,on_delete=models.CASCADE)

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    name=models.CharField(max_length=180)
    price=models.IntegerField(default=0)
    q=models.IntegerField(default=0)
    total_p=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
