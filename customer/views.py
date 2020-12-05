from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import ItemPostForm,CarsForm, AccountForm,HouseForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ItemPost
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



# Home page of customer
def index(request):
    form = UserCreationForm()
    accForm = AccountForm()
    post_list = ItemPost.objects.all().order_by('id').reverse()
    page = request.GET.get('page',1)
    paginator = Paginator(post_list,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm,'posts':posts})

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

# Temp fetch data
class fetchTempView(ListView):
    template_name ='customer/Posting_Item/fetchTemp.html'
    context_object_name = 'object_list'
    queryset = ItemPost.objects.all()
    paginate_by = 2

# done by biniam

def car(request):
    post_list = ItemPost.objects.all().filter(item_type='car').order_by('id').reverse()
    page = request.GET.get('page',1)
    paginator = Paginator(post_list,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'customer/common/car.html', {'posts':posts})

def house(request):
    post_list = ItemPost.objects.all().filter(item_type='house').order_by('id').reverse()
    page = request.GET.get('page',1)
    paginator = Paginator(post_list,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'customer/common/house.html', {'posts':posts})

# end done by biniam
