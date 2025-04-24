from django.shortcuts import render
from .forms import NameForm

def home(request):
    return render(request, 'home.html')

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            return render(request, 'thanks.html', {'name': name})
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})
