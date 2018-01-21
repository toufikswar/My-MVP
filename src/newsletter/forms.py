from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('full_name','email',)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, email_provider = email.split("@")
        domain, extension = email_provider.split(".")
        if domain != "gmail":
            raise forms.ValidationError("You must enter a Gmail address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        # if " " not in full_name:
        #     raise forms.ValidationError("Enter a valid name")
        return full_name


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, email_provider = email.split("@")
        domain, extension = email_provider.split(".")
        if domain != "gmail":
            raise forms.ValidationError("You must enter a Gmail address")
        return email
