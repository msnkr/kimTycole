from django.shortcuts import render
from django.views.generic import ListView
from tycole.forms import RequestContactForm

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
            return thank_you(request)
        else:
            raise ValidationError('Error')
    else:
        return render(request, 'tycole/contact_us.html', {'form': form})