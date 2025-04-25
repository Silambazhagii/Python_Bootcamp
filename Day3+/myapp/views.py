from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # after successful form submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'thank_you.html')
