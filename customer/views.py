from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ItemPostForm
# Create your views here.

def index(request):
    return HttpResponse('Hello Customer')

def itemPost(request):
    form=ItemPostForm(request.POST or None)
    if form.is_valid():
        form.save()
    #     return HttpResponse('saved')
    # else:
    #     return HttpResponse('not saved')
    context = {'form': form}
    return render(request,'customer/itemPost.html',context)

