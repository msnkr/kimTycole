import os
from django.shortcuts import render
from django.views.generic import ListView
from django.core.mail import send_mail
from tycole.forms import RequestContactForm
from .models import OurWork

# Create your views here.
def index(request):
    return render(request, 'tycole/index.html')


def printing(request):
    return render(request, 'tycole/printing.html')


def promotional(request):
    return  render(request, 'tycole/promotional.html')


def contactform(request):
    form = RequestContactForm()
    if request.method == 'POST':
        form = RequestContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['name']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            form_message = f'MESSAGE: {message}\n\nFROM: {from_email}\n\nNUMBER: {number}'
            send_mail(subject, form_message, os.getenv('EMAIL_USERNAME'), [os.getenv('EMAIL')])
            return thank_you(request)
        else:
            raise ValidationError('Error')
    else:
        return render(request, 'tycole/contact_us.html', {'form': form})

def thank_you(request):
    return render(request, 'tycole/thank_you.html')

class OurWorkListView(ListView):
    model = OurWork
    ordering = ['-date']


