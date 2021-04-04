from user.models import USER
from user.forms import UserForm
from authenticate import Authentication
from django.shortcuts import render,redirect

# Create your views here.
def after_login(request):
    return redirect("/Product/display_arts")

def create(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                print(form)
                return redirect("/display_art_seller")
            except:
                pass
    else:
        form = UserForm()
    return render(request, "ArtSeller/login.html", {'form': form})
