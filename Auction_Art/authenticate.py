from django.shortcuts import redirect
from user.models import USER
from django.contrib import messages
#class where authentication is done
class Authentication:
    def valid_user(function):
        def wrap(request):
            print(request)
            try:
                USER.objects.get(Email=request.session['Email'], Password = request.session['Password'])
                return function(request)
            except:
                messages.warning(request,'Please enter valid email and password')
            return redirect('/login')
        return wrap

    def valid_user_where_id(function):
        def wrap(request,product_id):
             try:
                USER.objects.get(Email=request.session['Email'], Password = request.session['Password'])
                print(USER.objects.get(Email=request.session['Email'], Password = request.session['Password'])
)
                return function(request,product_id)
             except:
                messages.warning(request,'Please enter valid email and password.')
                return redirect('/login')

        return wrap