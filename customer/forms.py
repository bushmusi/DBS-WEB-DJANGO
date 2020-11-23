from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import ItemPost

class ItemPostForm(forms.ModelForm):
    class Meta:
        model=ItemPost
        fields = ['title','item_name','item_price','item_type']


