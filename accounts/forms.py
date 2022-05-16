from pyexpat import model
from django import forms
from.models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Enter a password"
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Confirm password"
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone','email','password']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = "Enter first name"
        self.fields['last_name'].widget.attrs['placeholder'] = "Enter last name"
        self.fields['email'].widget.attrs['placeholder'] = "Enter email"
        self.fields['phone'].widget.attrs['placeholder'] = "Phone Number"
        self.fields['password'].widget.attrs['placeholder'] = "Enter a password"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


