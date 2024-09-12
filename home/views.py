from django.shortcuts import render
from django.http import HttpResponse
from datetime import  datetime

# Create your views here.


def home(request):
    # return HttpResponse("Hello world")
    return render(request, 'home/hello_world.html', {'today': datetime.today()})
