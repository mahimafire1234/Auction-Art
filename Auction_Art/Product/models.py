from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    product_name=models.CharField(max_length=200)
    product_description=models.TextField(max_length=800)
    image=models.FileField(upload_to="Images",default="image")
    minimum_price=models.PositiveIntegerField()
    bidStartDate = models.DateField(null=True)
    bidEndDate = models.DateField(null=True)
    class Meta:
        db_table="Product"


class Buyer(models.Model):
    user_id=models.AutoField(auto_created=True,primary_key=True)
    email=models.EmailField()

    class Meta:
        db_table="Buyer"

class Auction(models.Model):
    auction_id=models.AutoField(auto_created=True,primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    bidding_amount=models.PositiveIntegerField(null=True)

    class Meta:
        db_table="Auction"

class Auction1(models.Model):
    auction_id=models.AutoField(auto_created=True,primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    bidding_amount=models.PositiveIntegerField(null=True)

    class Meta:
        db_table="Auction_1"

class Product1(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    product_name=models.CharField(max_length=200)
    product_description=models.TextField(max_length=800)
    image=models.FileField(upload_to="Images",default="image")
    minimum_price=models.PositiveIntegerField()
    bidStartDate = models.DateTimeField(null=True)
    bidEndDate = models.DateTimeField(null=True)
    class Meta:
        db_table="Product_1"


user_types = (('admin', 'admin'), ('buyer', 'buyer'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(default='buyer', choices=user_types, max_length=100, null=True)

    class Meta:
        db_table = "Profile"


def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

class Cart(models.Model):
    cart_id=models.AutoField(auto_created=True,primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table="Cart"