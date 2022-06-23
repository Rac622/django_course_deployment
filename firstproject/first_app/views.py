from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord, User
from first_app.forms import FormName, SignUpForm
from . import forms
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_me':"Hello2 I am from views.py"}
    # return render(request,'first_app/index.html',context=my_dict)
    return render(request,'first_app/index.html',context=date_dict)

def form_page_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Validation Successful')
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])





    return render(request,'first_app/form_page.html',{'form':form})

def sign_up(request):
    form = forms.SignUpForm()

    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request) ## redirects you to the index page

        else:
            print("Error!! Form Invalid!")
    return render(request,'first_app/sign_up.html',{'form':form})
