from django.contrib import admin
from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('menu/',views.list_food,name='menu'),
    path('getfood/<int:id>',views.get_food,name='getfood'),
    path('create/',views.add_item,name='create'),
    path('update/<int:id>',views.update_item,name='update'),
    path('delete/<int:id>',views.delete_item,name='delete')
]


