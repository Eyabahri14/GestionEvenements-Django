from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("Affiche")

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('Affiche')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )


def login_user(req):
    if req.method == "POST":
        name = req.POST['username']
        pwd = req.POST['password']
        user = authenticate(req, username=name, password=pwd)
        if user is not None:
            login(req, user)
            return redirect('Affiche')

        else:
            messages.info(req, "Username or PWD incorrect")
            return redirect('login')
    else:
        return render(req, 'login.html')
