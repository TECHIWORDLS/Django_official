from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from todo_app.models import task


def home(request):
    return render(request, 'home.html')


def home_confrim(request):
    if request.method=='POST':
         name=request.POST.get('name')
         priority = request.POST.get('priority')
         obj = task(name=name,priority=priority)
         obj.save()
         return HttpResponse('done')
    return None