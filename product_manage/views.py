from django.shortcuts import render
from product_manage.models import *

# Create your views here.
def list(request):
    product_list = Product.objects.all()
    return render(request, 'list.html', locals())

