from django.shortcuts import render
from datetime import date
from django.views.generic import CreateView
from .models import Request, Contact
from .forms import RequestForm, ContactForm

today = date.today()
copyright = today.year

def HomeView(request):
    quote = """
        You wouldn't learn to wake before you fall.
    """
    return render(request, 'home/home.html', {
        "copyright": copyright,
        "quote": quote,
    })

def ContactView(request):
    return render(request, 'home/contact.html', {

    })

def AboutView(request):
    return render(request, 'home/about.html', {

    })

class RequestView(CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'home/request.html'

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'

def PortfolioView(request):
    return render(request, 'home/portfolio.html', {

    })


