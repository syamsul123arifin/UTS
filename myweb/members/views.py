from django.shortcuts import render
from django. http import HttpResponse
from django.template import loader


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def gallery(request):
    template = loader.get_template('gallery.html')
    return HttpResponse(template.render())

def sosmed(request):
    template = loader.get_template('sosmed.html')
    return HttpResponse(template.render())
def members(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())



# Create your views here.
