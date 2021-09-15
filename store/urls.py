from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('plants/', views.plants, name='plants'),
    path('seeds/', views.seeds, name='seeds'),
    path('cuttings/', views.cuttings, name='cuttings'),
    path('fruits/', views.fruits, name='fruits'),
    path('flowers/', views.flowers, name='flowers'),
    path('vegetables/', views.vegetables, name='vegetables'),
    path('medicine/', views.medicine, name='medicine'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]