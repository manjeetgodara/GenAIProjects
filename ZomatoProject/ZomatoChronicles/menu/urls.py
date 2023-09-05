from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('',views.dish_list,name='dish_list'),
    path('add/', views.add_dish, name='add_dish'),
    path('delete_dish/<int:dish_id>/', views.delete_dish, name='delete_dish'),
    path('update_dish/<int:dish_id>/',views.update_dish,name='update_dish'),
    path('place_order/', views.place_order, name='place_order'),
     path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
     path('orders/', views.order_list, name='order_list'),
      path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    


]
