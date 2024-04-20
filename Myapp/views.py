from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import todo
# Create your views here.
def home(request):
    context={}
    if(request.method=='POST'):
        task=request.POST.get('task')
        new_todo=todo(user=request.user,name=task)
        new_todo.save()
        all_todos=todo.objects.filter(user=request.user)
        context={
            'todos':all_todos
        }
    all_todos=todo.objects.filter(user=request.user)
    context={
            'todos':all_todos
        }
    return render(request,'todoapp/home.html',context)


def login_user(request):
    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        validate_user=authenticate(username=username,password=password)
        if validate_user is not None:
            login(request,validate_user)
            return redirect('home-page')
        else:
            messages.error(request,'username not exist')
            return redirect('log-in-page')
            
    return render(request,'todoapp/loginpage.html',{})


def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        get_all_by_username=User.objects.filter(username=username)
        if get_all_by_username:
            messages.error(request,'username already exist')
            return redirect('sign-up-page')
            
        if len(password) <3:
            messages.error(request,'to short password')
            return redirect('sign-up-page')
        print(username)
        new_user=User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,'SignUp successful')
        return redirect('log-in-page')
    return render(request,'todoapp/signup.html',{})
from django.shortcuts import get_object_or_404, redirect
from .models import todo

def DeleteTask(request, todo_name):
    try:
        
        get_todo = todo.objects.filter(user=request.user, name=todo_name)
    except todo.DoesNotExist:
        
        return redirect('home-page') 
    else:
        
        get_todo.delete()
        return redirect('home-page')

def Update(request,todo_name):
    try:
        
        get_todo = todo.objects.get(user=request.user, name=todo_name)
    except todo.DoesNotExist:
        return redirect('home-page') 
    else:
        get_todo.status=True
        get_todo.save()
        return redirect('home-page')

    