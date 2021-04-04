from django import forms
from Product.models import Product,Auction1,Buyer

# form for product
class Product_Form(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

# form for auction
class Auction_Form(forms.ModelForm):
    class Meta:
        model=Auction1
        fields = "__all__"

class Buyer_Registration(forms.ModelForm):
    class Meta:
        model=Buyer
        fields="__all__"