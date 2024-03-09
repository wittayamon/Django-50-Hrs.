from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def Login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username=="" or password=="":
            return redirect("/login")
        else:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                return redirect("login")
    else:
        return render(request,"usersapp/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/login")