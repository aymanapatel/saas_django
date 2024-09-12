from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Product


# Create your views here.


def home(request):
    # return HttpResponse("Hello world")
    return render(request, 'home/hello_world.html', {'today': datetime.today()})


@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})


def list_prod(request):
    all_products = Product.objects.all()
    return render(request, 'home/product_list.html', {'products': all_products})


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        print('@@@', product)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'home/product_detail.html', {'product': product})
