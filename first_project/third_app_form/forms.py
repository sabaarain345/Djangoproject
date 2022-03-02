import email
from unicodedata import name
from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name Need To Start with z! ")


class UserForm(forms.Form):
    name = forms.CharField(validators=[check_for_z],required=True)
    email = forms.EmailField(required=True)
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea,required=True)

    # Validating both email, are same or not Using clean method
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data.get('verify_email')

        if email != vemail:
            raise forms.ValidationError("MAKE SURE EMAIL MATCHED! ")

    # Created Hidden Fields
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # Validator method is replacement of clean_data
    

    #Basic method of Validation
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

    # this validation can be done by giving value in <p> of Hidden field explicitly like value="Hello friend"

