# main/views.py
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'


# main/views.py
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send an email)
            messages.success(request, "Thank you! Your message has been sent.")
            form = ContactForm()  # Clear the form after submission
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
