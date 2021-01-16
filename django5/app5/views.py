from django.shortcuts import render
from app5.forms import userform,user_profileinfoform
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    return render(request,'index.html')
@login_required
def special(request):
    return HttpResponse("YOU are logged in!!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):

    registered=False
    if request.method == "POST" :
        user_form=userform(data=request.POST)
        profile_form=user_profileinfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered=True
        else :
            print(user_form.errors,profile_form.errors)
    else :
        user_form = userform()
        profile_form = user_profileinfoform()
    return render(request,'registration.html',context={'registered':registered,'user_form':user_form,'profile_form':profile_form})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else :
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else :
            return HttpResponse("Invalid Username or Password")
    else:
        return render(request,'login.html',{})