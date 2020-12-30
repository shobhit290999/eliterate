from django.shortcuts import render
from django.http import HttpResponse
from .forms import Blog
from .models import Addblog
from user.models import UserAdd
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1 style='color:red'>Welcome to blog app</h1> ")

def addblog(request):
    if request.session.get("islogin"):
        form = Blog()
        return render(request,"blogform.html",{"form":form})
    else:
            
            return render(request,"nav.html")


def blogadd(request):
    if request.session.get("islogin"):
        form = Blog(request.POST)
        if form.is_valid():
            try:
               title = form.cleaned_data['title']
               post = form.cleaned_data['post']
               author = request.session['email']  #this is only the mail
        #while inserting the data into addblog you have to enter the object of useradd model
              
            except:
                title = form.cleaned_data['title']
                post = form.cleaned_data['post']
                author = request.session['to_']
                  #this is only the mail
        #while inserting the data into addblog you have to enter the object of useradd model
                Addblog.objects.create(title=title,post=post,author=UserAdd.objects.get(email=author))
                error = "Successfully uploaded the blog".upper()
                return render(request,"afterlogin.html",{"error":error})
            else:
                 Addblog.objects.create(title=title,post=post,author=UserAdd.objects.get(email=author))
                 error = "Successfully uploaded the blog".upper()
                 return render(request,"afterlogin.html",{"error":error})


        else:
            error = "Invalid Form"
            form = Blog()
            return render(request,"blogform.html",{"form":form,"error":error})
    else:
        
        return render(request,"nav.html")


def myblog(request):
    if request.session.get("islogin"):
        try:
           user = request.session['email']
        
        except:
           user = request.session['to_']   
           obj = UserAdd.objects.get(email=user)
           id = obj.id #primary key
           blogs = Addblog.objects.filter(author=id)
           allblogs = []
           for i in blogs:
               d = {
                'title' : i.title,
                'post' : i.post,
                'date' : i.date,
                'author' : i.author
               }
               allblogs.append(d)
           return render(request,"showblog.html",{"blogs":allblogs})

        else:  
              obj = UserAdd.objects.get(email=user)
              id = obj.id #primary key
              blogs = Addblog.objects.filter(author=id)
              allblogs = []
              for i in blogs:
                  d = {
                   'title' : i.title,
                   'post' : i.post,
                   'date' : i.date,
                   'author' : i.author
                  }
                  allblogs.append(d)
              return render(request,"showblog.html",{"blogs":allblogs})

             
        
    else:
        
        return render(request,"nav.html")




def allblog(request):
    if request.session.get("islogin"):
    
    
    
        blogs = Addblog.objects.filter()
        allblogs = []
        for i in blogs:
            d = {
                'title' : i.title,
                'post' : i.post,
                'date' : i.date,
                'author' : i.author,
                'slug'    : i.title,
            }
            allblogs.append(d)
        return render(request,"allblog.html",{"blogs":allblogs})   
    else:
        return render(request,"nav.html")

def parawise(request, slug):
    
    post = Addblog.objects.filter(title=slug).first()
    context = {'post':post}
    
    return render(request,'blogpost.html',context)    
    