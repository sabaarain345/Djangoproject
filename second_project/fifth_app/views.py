from atexit import register
import profile
from xml.dom.domreg import registered
from django.shortcuts import render
from django.urls import reverse
from fifth_app.forms import UserForm
from fifth_app.models import UserProfileInfo
from fifth_app.forms import UserProfileInfoForm
# import for login logout
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'fifth_app/index.html', context_dict)

@login_required
def special(request):
    return HttpResponse("You are logged In, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def base(request):
    return render(request, 'fifth_app/base.html')

def other(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        # user_form = UserForm(request.POST,instance=request.user)
        # profile_form = UserProfileInfoForm(request.POST,instance=request.user)


        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user 

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'fifth_app/other.html',
                           {'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})


# For User Login 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("username: {} and password {}". format(username, password))
            return HttpResponse("Invalid login detail supplied ")
    else: 
        return render(request,'fifth_app/login.html',{})

