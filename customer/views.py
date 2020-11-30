from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import ItemPostForm,CarsForm, AccountForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ItemPost
# Create your views here.



# Home page of customer
def index(request):
    form = UserCreationForm()
    accForm = AccountForm()
    return render(request,'common/user_rightside_nav.html',{'form':form,'accForm':accForm})

# Itempost method 
# then add dynamic dependent dropdown in view
def itemPostView(request):
    if request.method == 'POST':
        form = ItemPostForm(request.POST)
        carForm = CarsForm(request.POST)
        if form.is_valid() and carForm.is_valid():
            itemPost = form.save(commit=False)
            itemPost.user_id = User.objects.get(pk=request.user.id)
            itemPost.save()
            carModel = carForm.save(commit=False)
            carModel.item_post_id = ItemPost.objects.get(pk=itemPost.pk)
            carModel.save()
            messages.success(request, "Successfully saved!!!")
            return redirect('customer:itempost')
        else:
            return render(request,'customer/Posting_Item/itemPost.html',{'form':form,'carForm':carForm})

    else:
        form=ItemPostForm()
        carForm = CarsForm()
        context = {'form': form,'carForm':carForm}
        return render(request,'customer/Posting_Item/itemPost.html',context)

    
def ret(request):
    return render(request,'customer/itemPost.html')

