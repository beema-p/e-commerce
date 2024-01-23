from django.shortcuts import render, get_object_or_404
from .models import Category, Products
from django.core.paginator import Paginator, InvalidPage, EmptyPage


# Create your views here.

def allProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Products.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Products.objects.all().filter(available=True)
    paginator = Paginator(products_list, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'categories.html', {'category': c_page, 'products': products})


def ProdDetail(request, c_slug, prod_slug):
    try:
        product = Products.objects.get(category__slug=c_slug, slug=prod_slug)
    except Exception as E:
        raise E

    return render(request, 'product.html', {'product': product})
