from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mysite/index.html', {})

def about(request):
    return render(request, 'mysite/about.html', {})

def gallery(request):
    return render(request, 'mysite/gallery.html', {})

def contact(request):
    return render(request, 'mysite/contact.html', {})
