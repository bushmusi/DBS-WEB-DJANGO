from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ItemPost, Account, Cars
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponse, HttpResponseRedirect

# trial line of code



class ItemPostForm(forms.ModelForm):
    class Meta:
        model=ItemPost
        fields = ['title','item_name','item_price','item_type'] 
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
    manu_year = forms.DateField()
    class Meta:
        model = Cars
        fields = ['car_model','transmission','manu_year','engine_type','car_condition','drive_type','car_color','mileage','description']
        help_texts = {
            'engine_type': _('It is optional'),
            'drive_type': _('It is optional '),
            'car_color': _('It is optional'),
            'mileage': _('It is optional '),
            'description': _('It is optional '),
        }
        labels = {
            'manu_year': _('Manufactured date* '),
            'car_color': _('Color Condition* '),
            }
        widgets={
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 80})
        } 



