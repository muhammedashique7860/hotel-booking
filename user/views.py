from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminapp.models import AddRoom
from account.models import CustomerDetails
from .models import Book
from datetime import datetime
from account.models import User


# Create your views here.
def home(request):
    # obj2=CustomerDetails.objects.get(pk=id)
    obj=AddRoom.objects.all()
    context={'i':obj}
    return render(request,'user/home.html',context)


def book(request,id):
    obj=AddRoom.objects.get(pk=id)
    if request.method=='GET':
        return render(request,'user/book.html',context={'i':obj})
    elif request.method=='POST':
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']
        obj1=Book.objects.filter(checkin__gte=checkin, checkin__lte=checkout)
        obj2=Book.objects.filter(checkout__gte=checkin, checkout__lte=checkout)
        if len(obj1) == 0 and len(obj2) == 0:
            a = datetime.strptime(checkin, "%Y-%m-%d").date()
            b = datetime.strptime(checkout, "%Y-%m-%d").date()
            no_of_days = (b-a).days
            total = obj.rate * no_of_days
            return render(request,'user/book.html',context={'i':obj, 'total': total, 'msg': "Available",'checkin':checkin,'checkout':checkout})

        else:
            return render(request,'user/book.html',context={'i':obj, 'msg': "Not Available"})


def view_mybookings(request):
    obj=CustomerDetails.objects.get(user=request.user)
    obj2=Book.objects.filter(customer=obj)
    return render(request,'user/view_mybookings.html',context={'i':obj2})



def savebook(request):
    if request.method=='POST':
        checkin=request.POST['chckin']
        checkout=request.POST['chckout']
        amount=request.POST['amount']
        roomid=request.POST['roomid']
        obj2=Book(checkin=checkin,checkout=checkout,amount=amount)
        customer=CustomerDetails.objects.get(user=request.user)
        room=AddRoom.objects.get(pk=roomid)
        obj2.customer=customer
        obj2.room=room
        obj2.save()
        return redirect('user_home')
    else:
        return redirect('user_home')

def person_details(request):
    obj=CustomerDetails.objects.get(user=request.user)
    return render(request,'user/person_details.html',context={'i':obj})

def update_details(request):
    obj=CustomerDetails.objects.get(user=request.user)
    if request.method=='GET':
        return render(request,'user/update_details.html',context={'i':obj})  
    elif request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        adhar=request.POST['adhar']
        address=request.POST['address']
        email=request.POST['email']
        phnno=request.POST['mobileno']
        obj.fname=fname
        obj.lname=lname
        obj.age=age
        obj.adhar=adhar
        obj.address=address
        obj.email=email
        obj.phnno=phnno
        obj.save()
        return redirect('person_details')
def cancel_booking(request,id):
    obj=Book.objects.get(pk=id)
    obj.delete()
    return redirect('view_mybookings')
    



 




