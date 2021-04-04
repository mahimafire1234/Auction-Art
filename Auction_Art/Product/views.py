from django.shortcuts import render,redirect
from Product.models import Product,Auction1,Buyer
from Product.forms import Product_Form,Auction_Form,Buyer_Registration
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from datetime import date
from django.core.mail import send_mail
from authenticate import Authentication
from django.conf import settings

# Create your views here.
def displayHomePage(request):
    return render(request,"Home/homepage.html")
@Authentication.valid_user
# create arts
def createArt(request):
    if request.method == "POST":
        form = Product_Form(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            print("is valid")
            try:
                form.save()
                return redirect("/display_messages")
            except:
                pass
    else:
        form = Product_Form()
    return render(request, "ArtSeller/createArt.html", {'form': form})

# diplay created arts in seller dashboard
@Authentication.valid_user

def display_arts(request):
    product=Product.objects.all()
    return render(request,"ArtSeller/display.html",{"product":product})

# display messages
def display_art_message_success(request):
    return render(request,"ArtSeller/displayingMessage.html")
@Authentication.valid_user_where_id
# delete arts in seller dashboard
def delete_art_seller(request,product_id):
    product=Product.objects.get(product_id=product_id)
    product.delete()
    return redirect("/delete_message")

# displaying delete successful message
def delete_message(request):
    return render(request,"ArtSeller/displaydeleteMessage.html")
# edit the product seller
@Authentication.valid_user_where_id
def edit_art(request,product_id):
    product = Product.objects.get(product_id=product_id)
    form = Product_Form(instance=product)
    if request.method == "POST":
        form = Product_Form(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("/update_message")
    return render(request, "ArtSeller/updateArt.html", {'product': product})

# display succesful update
def update_message(request):
    return render(request,"ArtSeller/displayupdateMessage.html")

# view auction details
def view_auction_form(request,product_id):
    product=Product.objects.filter(product_id=product_id)
    return render(request,"ArtSeller/viewArts.html",{"product":product})

# home with arts
def home_arts(request):
    product=Product.objects.all()
    return render(request,"ArtSeller/home.html",{"product":product})

#auction part
# put an art up for auction
def create_auction(request,product_id):
    if request.method == "POST":
        product = Auction_Form(request.POST, request.FILES)
        if product.is_valid():
            try:
                product.save()
                return redirect("/message_auction")
            except:
                pass
    else:
        product = Auction_Form()
    return render(request, "ArtSeller/viewArts.html", {'form': product})

# auction message
def auction_message(request):
    return render(request,"ArtSeller/addedToAutction.html")

# biddings page
def view_biddings(request,product_id):
    product=Product.objects.filter(product_id=product_id)
    return render(request,"ArtSeller/biddings.html",{"product":product})

# bidding form
def view_bidding_form(request,product_id):
    product=Product.objects.filter(product_id=product_id)
    return render(request,"ArtSeller/biddingForm.html",{'product':product})

# create user
# views registration form for buyer
def buyer_registration(request):
    return render(request,"ArtSeller/bidderRegistration.html")

# creates the user in database
def buyer_create_Registration(request):
    if request.method == "POST":
        form = Buyer_Registration(request.POST, request.FILES)

        if form.is_valid():
            try:
                data=form.save()
                request.session["id"]=data.user_id

                return redirect("/home_arts")
            except:
                pass
    else:
        form = Buyer_Registration()
    return render(request, "ArtSeller/bidderRegistration.html", {'product': form})

# successful registration
def success_registration(request):
    return render(request,"ArtSeller/addedToAutction.html")

# create bid
def createbid(request):

    product=Product.objects.get(product_id=request.POST.get("product_id"))
    # getting the bid end date
    bidEnd = Product.objects.raw("select * from Product")
    timeNow = date.today()
    x = Auction1.objects.raw(
        "select * from Auction_1 where product_id_id= %s ORDER BY bidding_amount DESC LIMIT 1",
        [request.POST['product_id']])
    for m in x:
        user_email = m.user_id.email
        print(user_email)
        for j in bidEnd:
            enddate = j.bidEndDate
            print(j.bidEndDate, "end time")
            # win bid if auction expired

            if timeNow > enddate:
                print("true")
                print(f"EMAIL_HOST = {settings.EMAIL_PORT}")
                print("winner is" , user_email)

                send_mail(
                    'Bid Details',
                    'You have the highest bid. You have won the bid',
                    'seller@gmail.com',
                    [user_email]
                )

    if request.method=="POST":

        if int(request.POST["bidding_amount"]) <= Product.objects.get(
                product_id=request.POST['product_id']).minimum_price:
            print("bid amount too low")
            messages.error(request, "Your bid amount is low. Enter a larger amount.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            form = Auction_Form(request.POST)
            form.save()
            # change the minimum price with the highest bid amount
            win = Auction1.objects.raw(
                "select * from Auction_1 where product_id_id= %s ORDER BY bidding_amount DESC LIMIT 1",
                [request.POST['product_id']])
            for i in win:
                product.minimum_price = i.bidding_amount
                product.save()
                print(i.user_id + "you have highest bid")
                # print(product.minimum_price)
            print("your bid has been placed")
            request.session.clear()
            return redirect("/bidsuccess")
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def viewprice(request):
    minimum=Auction1.objects.all()

# bid unsuccessful
def bidlowmessage(request):
    product=Product.objects.filter(product_id=request.POST.get("product_id"))
    return render(request,"ArtSeller/bidlowmessage.html",{"product":product})

# bid successful
def bidsuccess(request):
    return render(request, "ArtSeller/sucessbid.html")

def viewlogin(request):
    return render(request,"ArtSeller/login.html")

def viewsignup(request):
    return render(request,"ArtSeller/signup.html")

def viewAboutUs(request):
    return render(request,"ArtSeller/aboutus.html")

def viewContact(request):
    return render(request,"ArtSeller/contactus.html")

def viewHelp(request):
    return render(request,"ArtSeller/help.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['repassword']
        usertype = request.POST['user-type']

        user = User.objects.create_user(username=username, password=password1, first_name=firstname, last_name=lastname,
                                        email=email)
        user.save()
        profile = Profile.objects.get(user=user)
        profile.user_type = usertype.lower()
        profile.save()
        return redirect("/home_arts")

    return render(request, "ArtSeller/signup.html")

# login for seller
def login(request):
    if request.method=="POST":
        request.session['Email']=request.POST['Email']
        request.session['Password']=request.POST['Password']
        return redirect("/display_art_seller")
    return render(request,"ArtSeller/login.html")

# log out for seller
def logout(request):
    request.session.clear()
    return redirect("/login")

# view biddings
def viewBiddingsSeller(request):
    win = Auction1.objects.raw("select * from Auction_1 ORDER BY product_id_id")
    return render(request,"ArtSeller/biddingSeller.html",{'win':win})

# check time
def checktime(request):
    product = Product.objects.all()
    # getting the bid end date
    bidEnd = Product.objects.raw("select * from Product")
    timeNow = date.today()


