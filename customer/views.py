from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import ItemPostForm,CarsForm, AccountForm,HouseForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ItemPost
# Create your views here.



# Home page of customer
def index(request):
    form = UserCreationForm()
    accForm = AccountForm()
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})

#Car Itempost method 

def carItemPostView(request):
    if request.method == 'POST':
        form = ItemPostForm(request.POST)
        carForm = CarsForm(request.POST)
        if form.is_valid() and carForm.is_valid():
            itemPost = form.save(commit=False)
            itemPost.user_id = User.objects.get(pk=request.user.id)
            itemPost.item_type = 'car'
            itemPost.save()
            carModel = carForm.save(commit=False)
            carModel.item_post_id = ItemPost.objects.get(pk=itemPost.pk)
            carModel.save()
            messages.success(request,'Car data succfully inserted!!!')
            return redirect('customer:carItemPost')
        else:
            return render(request,'customer/Posting_Item/carItemPost.html',{'form':form,'carForm':carForm})
    else:
        form=ItemPostForm()
        carForm = CarsForm()
        context = {'form': form,'carForm':carForm}
        return render(request,'customer/Posting_Item/carItemPost.html',context)


# huose itempost method
def houseItemPostView(request):
    if request.method == 'POST':
        form = ItemPostForm(request.POST)
        houseForm = HouseForm(request.POST)
        if form.is_valid() and houseForm.is_valid():
            itemPost = form.save(commit=False)
            itemPost.user_id = User.objects.get(pk=request.user.id)
            itemPost.item_type = 'house'
            itemPost.save()
            houseModel = houseForm.save(commit=False)
            houseModel.item_post_id = ItemPost.objects.get(pk=itemPost.pk)
            houseModel.save()
            messages.success(request,'House data succfully inserted!!!')
            return redirect('customer:houseItemPost')
        else:
            return render(request,'customer/Posting_Item/houseItemPost.html',{'form':form,'houseForm':houseForm})
    else:
        form=ItemPostForm()
        houseForm = HouseForm()
        context = {'form': form,'houseForm':houseForm}
        return render(request,'customer/Posting_Item/houseItemPost.html',context)

def ret(request):
    return render(request,'customer/houseItemPost.html')

