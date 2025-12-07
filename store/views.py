from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404

def store(request):

    all_products = Product.objects.all()

    context = {'my_products': all_products}

    return render(request,'store/store.html',context)

def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories':all_categories}


def list_category(request,category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html', {'category' : category, 'products' : products })


def product_info(request, product_slug):

    product = get_object_or_404(Product, slug=product_slug)

    context = {'product': product}

    return render(request, 'store/product-info.html', context)


def search(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.none()

    context = {
        'query': query,
        'products': products,
    }

    return render(request, 'store/search_results.html', context)


def sorted_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)

    sort_option = request.GET.get('sort')

    if sort_option == "low_to_high":
        products = products.order_by('price')
    elif sort_option == "high_to_low":
        products = products.order_by('-price')

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'store/list-category.html', context)



