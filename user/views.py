from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import views
from .forms import *
from django.views import View
from .models import UserAdd
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from .models import Rejistermodal
from .models import Contact

# Create your views here.
otp = ""
to_ = ""
def index(request):
    if request.session.get("islogin"):
        return render(request,"afterlogin.html")
    return render(request,"nav.html")
    #it will go to the path you have defined in settings.py file and will find the page and return it
    #return HttpResponse("User app")

def home(request):
    return HttpResponse("Welcome to my user app home")

def register(request):
    return render(request,"register.html")    

def registerpro(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        college = request.POST.get('college', '')
        gender = request.POST.get('gender', '')
        cources = request.POST.get('cources', '')
        rejister = Rejistermodal(name=name, email=email, phone=phone, college=college, gender=gender, cources=cources)
        rejister.save()
        return redirect('/user/')      

def contactpro(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        error="success"
    return redirect('/user/')  


def program(request):
    return render(request,"program.html")       

def jee(request):
    return render(request,"jee.html")

def neet(request):
    return render(request,"neet.html")

def cet(request):
    return render(request,"cet.html")

def gate(request):
    return render(request,"gate.html")

def gatecse(request):
    return render(request,"gatecse.html") 


def gateece(request):
    return render(request,"gateece.html")     

def gateee(request):
    return render(request,"gateee.html")      

def gatece(request):
    return render(request,"gatece.html")

def gateme(request):
    return render(request,"gateme.html")

def gatech(request):
    return render(request,"gatech.html")

def studymaterial(request):
    return render(request,"studymaterial.html")
             
def pyp(request):
    return render(request,"pyp.html")             

def contact(request):
    return render(request,"contact.html")             


def team(request):
    return render(request,"team.html")

def interns(request):
    return render(request,"interns.html")

def about(request):
    return render(request,"about.html")

def terms(request):
    return render(request,"terms.html")   

def login(request):
    if request.session.get("islogin"):
        return render(request,"afterlogin.html")
    else:
        form = Login()
        return render(request,"login.html",{'form':form})

def afterlogin(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid(): #validation
            email = form.cleaned_data['email']
            try:
                obj = UserAdd.objects.get(email=email)
            except Exception as e:
                error = "Invalid Email!!!!"
                form = Login()
                return render(request,"login.html",{"error":error,"form":form})
            else:
                passwd = form.cleaned_data['password']
                if obj.password == passwd:
                    request.session['email'] = email
                    request.session['islogin'] = "true"
                    return render(request,"afterlogin.html")
                else:
                    error = "Invalid password!!!"
                    form = Login()
                    return render(request,"login.html",{"error":error,"form":form})
            #return HttpResponse(f"{email}:{passwd}")
        else:
            error = "Invalid Form"
            form = Login()
            return render(request,"login.html",{'form':form,"error":error})
    else:
        return redirect("/user/login")
    
def signup(request):
    form = Signup()
    return render(request,"signup.html",{'form':form})

class aftersignup(View):
    # in View class the methods are the http methods
    def get(self,request):  #here get method is working for http get method request
        form = Signup()
        return render(request,"signup.html",{"form":form})
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            p1 = form.cleaned_data['password']
            p2 = form.cleaned_data['confirm_pass']
            if p1 == p2:
                try:
                    obj = UserAdd.objects.get(email=form.cleaned_data['email'])
                    #(email="simrangrover5@gmail.com")
                except Exception as e:
                    data = {
                        "email" : form.cleaned_data['email'],
                        "password" : p1,
                        "fname" : form.cleaned_data['fname'],
                        "lname" : form.cleaned_data["lname"],
                        "gender" : form.cleaned_data["gender"],
                        #"pic"  : form.cleaned_data["pic"]               
                        }
                    UserAdd.objects.create(**data)
                    return redirect("/user/login/")
                else:
                    error = "Email already exist"
                    form = Signup()
                    return render(request,"signup.html",{"form":form,"error":error})
            else:
                error = "Password does not match!!! Try Agaia"
                form = Signup()
                return render(request,"signup.html",{"form":form,"error":error})
        else:
            error = "Invalid Form"
            form = Signup()
            return render(request,"signup.html",{"form":form,"error":error})

def logout(request):
        try:
           del request.session['to_']
          
        except:
            del request.session['email']
            del request.session['islogin']
            return redirect("/user/")
        else:
            del request.session['islogin']
            return redirect("/user/")    

    
       

def forgot(request):
    form = Email_Form(request.POST)
    if form.is_valid():
        global to_
        from_ = "shobhit290999@gmail.com"
        to_ = form.cleaned_data['email']
        
        try:
            obj = UserAdd.objects.get(email=to_)
        except:
            error = "Email is not registered"
            form = Login()
            return render(request,"login.html",{'form':form,"error":error})
        else:
            global otp
            subject = "OTP to reset your password"
            otp = randint(1000,9999)
            message = f"Enter this otp to change your password {otp}"
            send_mail(subject,message,from_,[to_,],auth_password=settings.EMAIL_HOST_PASSWORD)
            request.session['to_'] = to_
            request.session['islogin'] = "true"
            form = Otp()
            return render(request,"getotp.html",{"form":form})

    else:
        error = "Invalid form"
        form = Login()
        return render(request,"login.html",{'form':form,"error":error})

def getform(request):
    form = Email_Form()
    return render(request,"otpform.html",{"form":form})

def afterotp(request):
    form = Otp(request.POST)
    if form.is_valid():
        otp1 = form.cleaned_data['otp']
        if otp1 == str(otp):
            form = changepassword()
            return render(request,"getpass.html",{"form":form})
        else:
            error = "Incorrect otp"
            form = Login()
            return render(request,"login.html",{"form":form,"error":error})
    else:
        error = "Invalid form"
        form = Login()
        return render(request,"login.html",{"form":form,"error":error})


def cp(request):
    form = changepassword()
    return render(request,"getpass.html",{"form":form})


def change(request):
    form = changepassword(request.POST)
    if request.session.get("islogin"):

       if request.method == "POST":
           if form.is_valid(): #validation
                   password1 = form.cleaned_data['password']
                
                   p3 = form.cleaned_data['password']
                   p4 = form.cleaned_data['confirm_pass']
                   if p3 == p4:
                       # write a code to fix it 
                    
                           user = request.session['to_']
                           obj = UserAdd.objects.get(email=user)
                         
                           obj.password = p3
                           obj.save()
                           
                           return render(request,"afterlogin.html")
                   else:
                       error = "password do not match" 
                       form = changepassword()
                       return render(request,"getpass.html",{'form':form , 'error':error})          
            #return HttpResponse(f"{email}:{passwd}")
           else:
               error = "Invalid Form"
               form = changepassword()
               return render(request,"getpass.html",{'form':form,"error":error})
       else:
           return redirect("/user/getpass")
    else:       
         return redirect("/user/getpass")     


