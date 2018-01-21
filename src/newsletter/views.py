from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

import os

from .forms import SignUpForm,ContactForm

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        title = "Hello %s" % (request.user)
    else:
        title = "Welcome"

    form = SignUpForm(request.POST or None)
    message = ""

    if form.is_valid():
        instance = form.save(commit=False)
        title = "Thank you %s" % (form.cleaned_data.get("full_name"))
        message = "You will receive info at %s, please check \
        the spam box." % (form.cleaned_data.get("email"))
        instance.save()


    context = {
                "title": title,
                "form": form,
                "message" : message,
    }

    return render(request, "home.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_full_name = form.cleaned_data.get("full_name")
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")

        # send_mail(
        #     'Contact form mail',
        #     form_message,
        #     settings.EMAIL_HOST,
        #     [form_email, "toufik.swar@icloud.com"],
        #     fail_silently=False,
        # )

    context = {
                "form":form,

    }
    print (os.path.join((os.path.dirname(settings.BASE_DIR)),"static_cdn"))


    return render(request, "contact.html", context)
