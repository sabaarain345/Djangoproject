from django.shortcuts import render
from django.http import HttpResponse
from third_app_form import forms

# Create your views here.
def index(request):
    return render(request, 'third_app/index.html')

def form_name_view(request):
    formss = forms.UserForm()

    if request.method =='POST':
        formss = forms.UserForm(request.POST)

        if formss.is_valid():
            # Doing Coding here
            print("Validation success!")
            print("NAME: "+formss.cleaned_data['name'])
            print("EMAIL: "+formss.cleaned_data['email'])
            print("TEXT: "+formss.cleaned_data['text'])
    return render(request, 'third_app/form.html', {'form': formss})



