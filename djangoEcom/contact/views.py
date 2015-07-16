from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.contrib import messages

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            messages.success(request, "Your application is submitted successfully.")
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
