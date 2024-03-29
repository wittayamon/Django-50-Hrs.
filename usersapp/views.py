from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def Login(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username=="" or password=="":
            messages.warning(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/login")
        else:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.warning(request,"บัญชีผู้ใช้ หรือ รหัสผ่าน ไม่ถูกต้อง")
                return redirect("login")
    else:
        return render(request,"usersapp/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/login")