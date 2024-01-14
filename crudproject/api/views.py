from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(request):
    std=Student.objects.all()

    return render(request,'home.html',{'std':std})

def add_std(request):
    if request.method == 'POST':
        roll=request.POST['roll']
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        reg=Student(roll=roll,name=name,email=email,address=address,phone=phone)
        reg.save()
        return redirect('/api/home')
    return render(request,'add_std.html')

def update_std(request,id):
    std=Student.objects.get(pk=id)

    return render(request,'update_std.html',{'std':std})

def do_update_std(request,id):
    roll=request.POST['roll']
    name=request.POST['name']
    email=request.POST['email']
    address=request.POST['address']
    phone=request.POST['phone']
    std=Student.objects.get(pk=id)
    std.roll=roll
    std.name=name
    std.emil=email
    std.address=address 
    std.phone=phone 
    std.save()
    return redirect('/api/home')
    return render(request,'update_std.html',{'std':std})

def delete_std(request,id):
    std=Student.objects.get(pk=id)
    std.delete()
    return redirect('/api/home')