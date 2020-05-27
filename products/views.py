from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Products
# Create your views here.



class IndexView(ListView):
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    

    def get_queryset(self):
        return Products.objects.all()


class DetailView(DetailView):
    model = Products
    template_name = 'products/detail.html'

class ProductCreate(CreateView):
    model = Products
    fields = ['name', 'size', 'price','bio','product_image']


class ProductUpdate(UpdateView):
    model = Products
    fields = ['name', 'size', 'price','bio','product_image']


class ProductDelete(DeleteView):
    model = Products
    success_url = '/shop'

























# def Index(request):
#     return render(request, 'index.html', {"home": "home Page"})


# def Product_list(request):
#     product = Products.objects.all();
#     context = {
#         'products': product
#     }
#     return render(request, 'product_list.html', context)

# def Detail(request, pk):
#     products = get_object_or_404(Products, pk=pk)
#     return render(request, 'detail.html', {'products': products})

