from django.urls import path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    #path('', views.product_list, name='product_list'),
    #path('', views.home, name='home'),
    #re_path(r'^home/$', views.home, name='home'),
    #path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    #path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    #path('product_list', views.product_list, name='product_list'),

    path('', views.product_list, name='product_list'),
    path('', views.home, name='home'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),


]
