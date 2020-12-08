from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect

# trial line of code


# Done by biniam

class PictureForm(forms.ModelForm):
    class Meta:
        model=Picture
        fields = ['path_addr'] 
        
# end of done by biniam


class ItemPostForm(forms.ModelForm):
    class Meta:
        model=ItemPost
        fields = ['item_name','item_price','item_type','serviceType'] 
        error_messages = {
            'title': {
                'max_length': _('fixed length enter')
            }
        }

class AccountForm(forms.ModelForm):
    # phone_num = forms.CharField(max_length=100, help_text='Enter your number +251...')
    class Meta:
        model = Account
        fields = ["phone_num"]
        labels = {
        'phone_num': _('Phone number: '),
        }
        help_texts = {
            'phone_num': _('Enter valid phone number ex: 0910....'),
        }
class CarsForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['car_model','transmission','manu_year','engine_type','car_condition','drive_type','car_color','mileage','car_description']
        help_texts = {
            'engine_type': _('It is optional'),
            'drive_type': _('It is optional '),
            'car_color': _('It is optional'),
            'mileage': _('It is optional '),
        }
        labels = {
            'car_color': _('Color Condition* '),
            'manu_year': _('Manufactured date* '),
            }
        widgets={
            'car_description': forms.Textarea(attrs={'cols': 80, 'rows': 80})
        } 
        
class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['area','bank_loan','bed_unit','house_description','lat','longt']
        help_texts = {
            'area': _('Size of area in meter'),
        }
        labels = {
            'area': _('Size Of The Area* '),
            'lat': _('Latitude'),
            'longt': _('Longitude ')
            }
        widgets={
            'house_description': forms.Textarea(attrs={'cols': 80, 'rows': 80})
        }


