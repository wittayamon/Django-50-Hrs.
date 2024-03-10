from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import *
# Create your views here.
# M T V (Models Template Views)
def Home(request):
    products=Product.objects.filter(trendingnow=True)
    context = {"products":products}
    return render(request,'myapp/home.html',context)
def Products(request):
    return render(request,'myapp/product.html')
@login_required(login_url="/login")
def TrackingPage(request):
    tracks = Tracking.objects.all()
    context = {'tracks':tracks}
    return render(request,'myapp/tracking.html',context)
def Learnmore(request):
    return render(request,'myapp/learnmore.html')
def Contact(request):
    return render(request,'myapp/contact.html')
def Ask(request):
    if request.method == 'POST':
        data = request.POST.copy()
        # print('DATA:' ,data)
        name = data.get('name') #name=name
        email = data.get('email')
        title = data.get('title')
        detail = data.get('detail')
        new_ask = askQA()
        new_ask.name = name
        new_ask.email = email
        new_ask.title = title
        new_ask.detail = detail
        new_ask.save()
    return render(request,'myapp/ask.html')
@login_required(login_url="/login")
def addTracks(request):
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        tel = data.get('tel')
        newtrack = data.get('newtrack')
        detail_track = data.get('detail_track')
        # ดึง model
        new_track = Tracking()
        new_track.name = name
        new_track.tel = tel
        new_track.tracking = newtrack
        new_track.other = detail_track
        new_track.save()
    return render(request,'myapp/formtrack.html')
@login_required(login_url="/login")
def edit(request,tracks_id):
    # เช็คว่าส่ง method post มาหรือเปล่า
    if request.method == 'POST':
        tracks = Tracking.objects.get(id=tracks_id)
        tracks.name = request.POST["name"]
        tracks.tel = request.POST["tel"]
        tracks.tracking = request.POST["newtrack"]
        tracks.other = request.POST["detail_track"]
        tracks.save()
        return redirect("/tracking")
    else:
        # ดึงข้อมูลที่จะแก้ไข
        tracks = Tracking.objects.get(id=tracks_id)
        context = {'tracks':tracks}
        return render(request, 'myapp/editformtrack.html',context)
@login_required(login_url="/login")
def delete(request,tracks_id):
    tracking = Tracking.objects.get(id=tracks_id)
    tracking.delete()
    return redirect("/tracking")
