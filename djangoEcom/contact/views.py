from django.shortcuts import render
from contact.forms import ContactForm

def contact_us(request):
    form = ContactForm()
    template = 'contact/contact.html'
    return render(request, template, {'form': form})
