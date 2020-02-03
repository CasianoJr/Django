from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q


def product_all(request):
    context = {
        'products':  Product.objects.all()
    }
    return render(request, 'product_all.html', context)


def product_detail(request, slug):
    products = get_object_or_404(Product, slug=slug)
    context = {
        'item': products
    }
    return render(request, 'product_detail.html', context)


def store_search(request):
    queryset = ''
    query = request.GET.get('search')
    latest_product = Product.objects.all().order_by('-timestamp')[:10]
    if query:
        query = query.strip(' ')
        queryset = Product.objects.filter(Q(name__icontains=query) | Q(
            description__icontains=query) | Q(specification__icontains=query)).distinct()
    context = {
        'queryset': queryset,
        'query': query,
        'latest_product': latest_product
    }
    return render(request, 'store_search.html', context)


def cart(request):
    context = {
        'sample': 'sample'
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order = Product.object.get_or_create(
        user=request.user.profile,
        item=item,
        ordered=False
    )
