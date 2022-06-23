from django import forms
from django.core import validators
from first_app.models import User

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Confirm email")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)]) ## using the django built-in validators, instead of the clean_botcatcher method.


    # def clean_botcatcher(self):
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     return botcatcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure the emails match!")

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
