
from django.shortcuts import render,HttpResponse
from . models import Department,Role,Empolly
import datetime


# Create your views here.
def index(request):
    emps=Empolly.objects.all()
    context={
        'emps':emps
    }
    print (context)
    return render(request,'index.html',context)

def ViewEmp(request):
    return render(request,'view.html')

def AddEmp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_Name=request.POST['last_Name']
        dept=request.POST['dept']
        salary=request.POST['salary']
        bondus=request.POST['bondus']
        role=request.POST['role']
        phone=request.POST['phone']
        hiredate=request.POST['hiredate']
        newemp=Empolly(first_name=first_name,last_Name=last_Name,dept=dept,salary=salary,bondus=bondus,role=role,phone=phone,hiredate=datetime.now())
        newemp.save()
        return HttpResponse('Success ful data save')
    elif request.method =='GET':
        return render(request,'add.html')
    else:
        return HttpResponse('Exception handle')

def Remove(request):
    return render(request,'remove.html')

def Filters(request):
    return render(request,'filters.html')
