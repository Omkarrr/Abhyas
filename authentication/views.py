from ast import Return
import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import django.contrib.staticfiles

# Create your views here.
def home(request):
    return render(request, "authentication/Main.html")

def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create(username, email, pass1)
        myuser.firstname = fname
        myuser.lastname = lname

        myuser.save()

        messages.success(request, "Your Account has been Successfuly Created")

        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass

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
    return render(request, "authentication/signup.html")