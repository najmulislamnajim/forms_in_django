from django import forms
from django.core import validators

class createAccount(forms.Form):
    name=forms.CharField(label='User Name')
    email=forms.EmailField(validators=[validators.EmailValidator()])
    birthday=forms.DateField(label='Birth Date', widget=forms.DateInput(attrs={'type':'date'}))
    GENDER=[('m','male'),('f','female')]
    gender=forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect)
    password=forms.CharField(widget=forms.PasswordInput)
    confirmPassword=forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    profilePicture=forms.FileField(label='Upload Photo')
    
    def clean(self):
        cleaned_data=super().clean()
        passval=self.cleaned_data['password']
        cpassval=self.cleaned_data['confirmPassword']
        print(passval,cpassval)
        
        if passval != cpassval:
            print('najmul islam')
            raise forms.ValidationError('Password does not match!')
    