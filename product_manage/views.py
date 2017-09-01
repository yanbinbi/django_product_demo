from django.shortcuts import render
from product_manage.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

# Create your views here.
def get_page(request, product_list):
    # 实例化分页对象
    pagenator = Paginator(product_list, 2)
    try:
        page = int(request.GET.get("page", 1))
        product_list = pagenator.page(page)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        product_list = pagenator.page(1)
    return product_list

def list(request):
    product_list = Product.objects.all()
    product_list = get_page(request, product_list)
    return render(request, 'list.html', locals())

