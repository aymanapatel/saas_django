from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Product
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/hello_world.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def my_view(request):
    # Create a custom span
    with tracer.start_as_current_span("custom-span"):
        return HttpResponse("Hello, World!")    

# def home(request):
#     # return HttpResponse("Hello world")
#     return render(request, 'home/hello_world.html', {'today': datetime.today()})
#
#
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})


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
