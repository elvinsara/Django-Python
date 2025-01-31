from django.shortcuts import render,redirect
from . models import FoodItems
from . forms import ItemForm
# Create your views here.
def list_food(request):
    item_list = FoodItems.objects.all()
    return render(request,'menu.html',{'food':item_list})


def get_food(request,id):
    food_item = FoodItems.objects.get(pk=id)
    return render(request,'item_info.html',{'food_item_info':food_item})

def add_item(request):
    form = ItemForm()
    if request.POST:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food:menu')
    return render(request,'item_form.html',{'form':form})

def update_item(request,id):
    item = FoodItems.objects.get(pk=id)
    form = ItemForm(instance=item)
    #return render(request,'test.html',{'id':item})
    if request.method == "POST":
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('food:menu')
    return render(request,'item_form.html',{'form':form,'item':item})

def delete_item(request,id):
    item = FoodItems.objects.get(pk=id)
    if request.method == "POST":
        item.delete()
        return redirect('food:menu')
    return render(request,'confirm_delete.html')

