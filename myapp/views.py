from django.shortcuts import render,redirect
from .models import registertable
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method =='POST':
        uname = request.POST.get("username")
        uemail = request.POST.get("useremail")
        upassword = request.POST.get("userpassword")
        ucpassword = request.POST.get("userpassword2")

        if upassword != ucpassword:
            messages.error(request,"pass not match")
        else:
            query = registertable(
                name=uname,
                email=uemail,
                password=upassword,
                password2=ucpassword
            )
            query.save()
            messages.success(request,'data inserted succesfull ')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get("uname")
        password = request.POST.get("password")

        user = registertable.objects.get(
            name=username,
            password2=password
        )
        if user is not None:
            messages.success(request,"login successfull")
            return render(request,'home.html')
        else:
            messages.error(request,"error")
    return render(request,'login.html')

def logout(request):
    return render(request,'login.html')

def data(request):
    all = registertable.objects.all()
    return render(request,"data.html",{'all':all})

def delete_data(request,name):
    s=registertable.objects.get(pk=name)
    s.delete()
    return redirect("register.html")