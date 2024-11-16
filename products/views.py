from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
#def product_view(requests):
#    return HttpResponse('Hello World!!!!!!!!! JOWWWWHHH')

def product_view(request):
    print(dir(request))
    var_products = Product.objects.all()
    return render(
        request=request,
        template_name='products.html',
        context= {'products': var_products}
        )

