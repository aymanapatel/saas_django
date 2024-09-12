from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.


def home(request):
    # return HttpResponse("Hello world")
    return render(request, 'home/hello_world.html', {'today': datetime.today()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})
