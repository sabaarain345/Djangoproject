from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Connecting this view file to database record
from second_app.models import Topic, Webpage, AccessRecord, User
# importing for Model Form to connect the form to model
from second_app.forms import NewUserForm


# Create your views here.
def help(request):
        my_dict = {'insert_me': "Hello! I am coming from Second_app/help.html"}
        return render(request,'second_app/help.html', context=my_dict)

def about(request):
        about_dict = {'help_me': "Hello! This is About page"}
        return render(request,'second_app/help.html', context=about_dict)

def current_datetime(request):
        now = {'date': datetime.datetime.now()}
        return render(request,'second_app/date.html', context=now)

def images(request):
        img_dict = {'image': "Hello! this is image"}
        return render(request,'second_app/django.html', context=img_dict)

# View for Accessing database
def data_acc(request):
        webpages_list = AccessRecord.objects.order_by('date')
        date_dict = {'access_records': webpages_list}
        return render(request,'second_app/database.html', context=date_dict)

def users(request):
        user_list = User.objects.order_by('first_name')
        user_dict = {'user_acc': user_list}
        return render(request,'second_app/user.html',context=user_dict)


def index(request):
        return render(request,'second_app/modelform.html')

def model_form(request):
        form = NewUserForm()

        if request.method == "POST":
                form = NewUserForm(request.POST)

                if form.is_valid():
                        form.save(commit=True)
                        return index(request)
                else:
                        print("ERROR FORM INVALID")
        return render(request, 'second_app/modelform.html', {'form': form})

