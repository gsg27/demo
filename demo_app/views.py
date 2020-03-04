from django.shortcuts import render
from django.http import HttpResponse
from .models import detail
from .forms import detail_form
# Create your views here.
def home(request):
    form = detail_form()
    if request.method == 'POST':
        form = detail_form(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'home.html',{'f':form})
    else:
        return render(request,'home.html',{'f':form})

def name_data(request):
    data = (detail.objects.all())
    
    return render(request,'detail.html',{'data':data})