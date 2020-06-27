from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-field','autocomplete':'off','placeholder':'Username'})
        self.fields['first_name'].widget.attrs.update({'class': 'input-field','autocomplete':'off','placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'input-field','autocomplete':'off','placeholder':'Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'input-field','autocomplete':'off','placeholder':'Email'})
        self.fields['password'].widget.attrs.update({'class': 'input-field','autocomplete':'off','placeholder':'Password'})
        

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        widgets = {
            'password':forms.PasswordInput(),
        }
        help_texts = {
            'username':None
        }

        


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password':forms.PasswordInput(),
        }