from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    
    path('', views.IndexView.as_view(), name='product_list'),
    path('products_list/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('products/add/', views.ProductCreate.as_view(), name='product_add' ),
    path('products/<int:pk>/update', views.ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete')




]