from django.shortcuts import render, redirect
from .models import posts, events, users
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.

def index(request):
    Latestpost = posts.objects.all()[:3]
    event1 = events.objects.get(id = 1)
    event2 = events.objects.get(id = 2)
    event3 = events.objects.get(id = 3)
    event4 = events.objects.get(id = 4)
    event5 = events.objects.get(id = 5)
    
    context = {
        'Posts': Latestpost,
        'event1':event1,
        'event2':event2,
        'event3': event3,
        'event4': event4,
        'event5': event5,
    }

   
    return render (request, "post/posts.html",context) 

def postpage(request,post_title):
    postpage = posts.objects.get(title = post_title)
    return render(request, "post/postpage.html",{
        "postpage" : postpage
    })

def eventfull (request,event_title):
    eventfull = events.objects.get(title = event_title)
    return render (request, "post/eventsingle.html", {
        "eventfull" : eventfull
    })


def blogpage (request):
    allblogpost = posts.objects.all()
    context = {
        'blogfull' : allblogpost,
    }
    return render (request, "post/blogpage.html", context)

 
def eventpage (request):
    alleventpost = events.objects.all()
    context = {
        'eventfull' : alleventpost,
    }
    return render (request, "post/eventpage.html", context)



def admission (request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
    
    else :
        form = CommentForm()

    return render (request, "post/admission.html",{
        'form': form
    })

def contact (request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/contact/')
    
    else :
        form = CommentForm()

    return render (request, "post/contact.html",{
        'form': form
    })
    

def prospects (request):
    return render (request, "post/prospects.html",)

def apply (request):
    form = UserApply()
    if request.method == 'POST':
        form = UserApply(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/apply/')
            
    else :
        form = UserApply()

    return render (request, "post/apply.html",{
        'form': form
    })

def dashboard (request):
   
    return render(request,"post/dashboard.html")

def administrator (request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render (request, "post/dashboard.html")

def login_view (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("administrator"))

        else:
            return (request, "post/login.html", {
                "message" : " Invalid Credentials."
            })
     
    return render (request,"post/login.html") 

def logout_view (request):
    logout(request)
    return render (request, "post/login.html", {
         "message" : " Logged Out"
    })


def upload_post (request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/administrator/post_list/')
    
    else :
        form = PostForm()
    
    return render (request,"post/upload_post.html",{
        'form' : form
    })


def upload_event (request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/administrator/event_list/')
            
        
    else :
        form = EventForm()   
    
    
    return render (request,"post/upload_event.html",{
        'form' : form
    })


def add_user (request):
    
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/administrator/user_list/')
    
    else :
        form = UserForm()
        
    return render (request,"post/add_user.html",{
        'form' : form
    })


def add_comment (request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/administrator/comment_list/')
    
    else :
        form = CommentForm()
        
    return render (request,"post/add_comment.html",{
        'form' : form
    })



def apply_user (request):
    form = UserApply()
    if request.method == 'POST':
        form = UserApply(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/apply/')
    
    else :
        form = UserApply()
    
    return render (request,"post/apply.html",{
        'form' : form
    })



def post_list (request):
    postlist = posts.objects.all()
    
    context = {
        'postlist' : postlist,
    }
    return render (request, "post/post_list.html", context)



def event_list (request):
    eventlist = events.objects.all()
    
    context = {
        'eventlist' : eventlist,
    }
    return render (request, "post/event_list.html", context)


def user_list (request):
    userlist = users.objects.all()
    applylist = userapply.objects.all()
    
    context = {
        'userlist' : userlist,
        'applylist': applylist,
    }
    return render (request, "post/user_list.html", context)


def comment_list (request):
    commentlist = comments.objects.all()
    
    context = {
        'commentlist' :commentlist,
    }
    return render (request, "post/comment_list.html", context)



