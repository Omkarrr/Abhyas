from ast import Return
import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import login, logout
import authentication


# Create your views here.
def home(request):
    return render(request, "authentication/Main.html")



def aboutus(request):
    return render(request, "authentication/aboutus.html")

def std10(request):
    return render(request, "authentication/std10.html")

def std11(request):
    return render(request, "authentication/std11.html")

def std12(request):
    return render(request, "authentication/std12.html")

def Btech(request):
    return render(request, "authentication/Btech.html")

def it(request):
    return render(request, "authentication/it.html")

def sem1it(request):
    return render(request, "authentication/sem1it.html")

def sem2it(request):
    return render(request, "authentication/sem2it.html")

def sem3it(request):
    return render(request, "authentication/sem3it.html")

def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['Username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been Successfuly Created")

        return redirect('/signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authentication(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/signin.html", {'fname':fname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('/')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    return redirect('/')