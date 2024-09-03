from multiprocessing import context
from django.shortcuts import render,redirect
from .models import AddRoom
from account.models import CustomerDetails
from user.models import Book



# Create your views here.
def home(request):
    return render(request,'adminapp/home.html')
def add_room(request):
    if request.method=='GET':
        return render(request,'adminapp/add_room.html')
    elif request.method=='POST':
        rno=request.POST['roomno']
        des=request.POST['des']
        ac=request.POST['ac']
        type=request.POST['type']
        bed=request.POST['bed']
        rate=request.POST['rate']
        img=request.FILES['img']
        obj1=AddRoom(rno=rno,des=des,ac=ac,roomtype=type,bedtype=bed,rate=rate,image=img)
        obj1.save()
        return redirect('adm')
def view_room(request):
    obj=AddRoom.objects.all()
    context={'i':obj}
    return render(request,'adminapp/view_room.html',context)
def view_customer(request):
    obj=CustomerDetails.objects.all()
    context={'i':obj}
    return render(request,'adminapp/view_customer.html',context)
def update_room(request,id):
    obj=AddRoom.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'adminapp/updateroom.html',context={'j':obj})  
    elif request.method=='POST':
        rno=request.POST['roomno']
        des=request.POST['des']
        ac=request.POST['ac']
        type=request.POST['type']
        bed=request.POST['bed']
        rate=request.POST['rate']
        img=request.FILES['img']
        obj.rno=rno
        obj.des=des
        obj.ac=ac
        obj.roomtype=type
        obj.bedtype=bed
        obj.rate=rate
        obj.image=img
        obj.save()
        return redirect('adm')
def view_bookings(request):
    obj=Book.objects.all()
    context={'i':obj}
    return render(request,'adminapp/view_bookings.html',context)
def delete_customer(request,id):
    obj=CustomerDetails.objects.get(pk=id)
    obj.delete()
    return redirect('view_customer')
def delete_room(request,id):
    obj=AddRoom.objects.get(pk=id)
    obj.delete()
    return redirect('view_room')
