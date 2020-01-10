from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from UserAuth.forms import RegisterForm

def index(request):
    return render(request,'index.html')

@login_required(login_url="/user/login/")
def upload(request):
    # if not request.user.is_authenticated():
    #     return HttpResponseRedirect('/accounts/')
    context={}
    if request.method == 'POST':
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
    return render(request,'upload.html',context)

def register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('success')
    else:
        form=UserCreationForm()

    context={'form':form}
    return render(request,'registration/register.html',context)

def success(request):
    return render(request,"success.html")

def user_login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            user=form.get_user()
            login(request, user)
            return redirect('upload')
    else:
        form=AuthenticationForm()
    return render(request,'registration/login.html',{'form':form})