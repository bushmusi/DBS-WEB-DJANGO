from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import ItemPostForm,CarsForm, AccountForm,HouseForm, PictureForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ItemPostFilter
from django.forms import modelformset_factory
# bini

def submitWishList(request):
    itemPost = ItemPost.objects.filter(id = 10).first()
    wishList = WatchList.objects.create(item_post_id = itemPost,user_id = request.user)
    wishList.save()
    return redirect('customer:index')

# Create your views here.
def houseIndexView(request):
    form = UserCreationForm()
    accForm = AccountForm()
    housePosts = House.objects.all().select_related()
    itemList = ItemPost.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(housePosts,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm,'posts':posts,'itemList':itemList})

def carIndexView(request):
    form = UserCreationForm()
    accForm = AccountForm()
    carPosts = Cars.objects.all().select_related()
    itemList = ItemPost.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(carPosts,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm,'posts':posts,'itemList':itemList})

# Home page of customer
def index(request):
    form = UserCreationForm()
    authForm = AuthenticationForm()
    accForm = AccountForm()
    itemList = ItemPost.objects.all()
    myFilter = ItemPostFilter(request.GET, queryset=itemList)
    itemList = myFilter.qs
    page = request.GET.get('page',1)
    paginator = Paginator(itemList,3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm,'posts':posts,'myFilter':myFilter,'authForm':authForm})
    # return HttpResponse(None)

#Car Itempost method 

def carItemPostView(request):
    if request.method == 'POST':
        form = ItemPostForm(request.POST)
        carForm = CarsForm(request.POST)
        picForm = PictureForm(request.POST or None,request.FILES or None)
        if form.is_valid() and carForm.is_valid():
            itemPost = form.save(commit=False)
            itemPost.user_id = User.objects.get(pk=request.user.id)
            itemPost.item_type = 'car'
            itemPost.save()
            carModel = carForm.save(commit=False)
            carModel.item_post_id = ItemPost.objects.get(pk=itemPost.pk)
            carModel.save()
            picModel = picForm.save(commit=False)
            picModel.item_post_id = ItemPost.objects.get(pk=itemPost.pk)
            picModel.save()
            messages.success(request,'Car data succfully inserted!!!')
            return redirect('customer:carItemPost')
        else:
            return render(request,'customer/Posting_Item/carItemPost.html',{'form':form,'carForm':carForm,'picForm':picForm})
    else:
        form=ItemPostForm()
        carForm = CarsForm()
        picForm = PictureForm()
        context = {'form': form,'carForm':carForm,'picForm':picForm}
        return render(request,'customer/Posting_Item/carItemPost.html',context)


# huose itempost method
def houseItemPostView(request):
    if request.method == 'POST':
        form = ItemPostForm(request.POST)
        houseForm = HouseForm(request.POST)
        picForm = PictureForm(request.POST or None,request.FILES or None)
        if form.is_valid() and houseForm.is_valid():
            itemPost = form.save(commit=False)
            itemPost.user_id = User.objects.get(pk=request.user.id)
            itemPost.item_type = 'house'
            itemPost.save()
            houseModel = houseForm.save(commit=False)
            houseModel.item_post_id = ItemPost.objects.get(pk=itemPost.pk)
            houseModel.save()
            picModel = picForm.save(commit=False)
            picModel.item_post_id = ItemPost.objects.get(pk=itemPost.pk)
            picModel.save()
            messages.success(request,'House data succfully inserted!!!')
            return redirect('customer:houseItemPost')
        else:
            return render(request,'customer/Posting_Item/houseItemPost.html',{'form':form,'houseForm':houseForm})
    else:
        form=ItemPostForm()
        houseForm = HouseForm()
        picForm = PictureForm()
        context = {'form': form,'houseForm':houseForm,'picForm':picForm}
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
    pictures = Picture.objects.all()
    post_list = ItemPost.objects.all().filter(
        item_type='house').order_by('id').reverse()
    # done by biniam searchFilter
    myFilter = ItemPostFilter(request.GET, queryset=post_list)
    post_list = myFilter.qs
    # end of done by biniam SearchFilter
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'customer/common/house.html', {'posts': posts, 'pictures': pictures, 'myFilter': myFilter})

# end done by biniam
