from django.shortcuts import render
from django.http import HttpResponse
from . forms import createAccount
# Create your views here.
def form(request):
    return render(request,'form.html')

def greetings(request):
    return render(request,'greetings.html')

def contact_received(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        surname=request.POST.get('surname')
        email=request.POST.get('email')
        message=request.POST.get('message')
        return render(request,'contact_received.html',{'firstname':firstname,'surname':surname,'email':email,'message':message})
    else:
        return HttpResponse('Error 4')
    
def django_form(request):
    if request.method == 'POST':
        form=createAccount(request.POST, request.FILES)
        if form.is_valid():
            file=form.cleaned_data['profilePicture']
            with open('./form/upload/' + file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form=createAccount()
    return render(request,'django_form.html',{'form':form})