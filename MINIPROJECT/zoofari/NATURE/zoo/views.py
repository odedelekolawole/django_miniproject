from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth import authenticate, login
from . models import Animal1, SpecialServices, Gallery

# Create your views here.
def error_404_view(request, exception):
    return render(request, "zoo/error.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "User with this credential already exits")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect(reverse(signup))
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect(reverse(signin))
        else:
            messages.info(request, "Both passwords must match")
            return redirect(reverse(signup))
    else:
        return render(request, "zoo/signup.html")




def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(reverse(home))
        else:
            messages.info(request, "Credential Invalid")
            return redirect(reverse(signin))
    else:
        return render(request, "zoo/signin.html")



def logout(request):
    auth.logout(request)
    return redirect(reverse(home))


def base(request):
    time = Animal1.objects.all()
    context = {
        "time": time 
    }
    return render(request, "zoo/base.html", context)



    
def home(request):
    animals = Animal1.objects.all()
    services = SpecialServices.objects.all()
    gallery = Gallery.objects.all()
    context = {
        "animals": animals,
        "services": services,
        "gallery": gallery
    }

    return render(request, "zoo/home.html", context)

def about(request):
    return render(request, "zoo/about.html")

def services(request):
    return render(request, "zoo/services.html")

def animals(request):
    return render(request, "zoo/animals.html")

def membership(request):
    return render(request, "zoo/membership.html")

def visiting(request):
    return render(request, "zoo/visiting.html")

def testimonial(request):
    return render(request, "zoo/testimonial.html")

def error(request):
    return render(request, "zoo/error.html")

def contact(request):
    return render(request, "zoo/contact.html")
