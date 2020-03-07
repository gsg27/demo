from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import detail
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import detail_form
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    form = detail_form()
    if request.method == 'POST':
        form = detail_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html',{'f':form})
    else:
        return render(request,'home.html',{'f':form})

@login_required(login_url='/login/')
def name_data(request):
    data = (detail.objects.all())
    
    return render(request,'detail.html',{'data':data})

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            # messages.success(request, 'Account created successfully')
            return redirect('/login')
    else:
        f = UserCreationForm()
 
    return render(request, 'register.html', {'form': f})