from django.shortcuts import render


# Create your views here.
def index(request):
    #render the HTML template index.html
    return render(request, 'index.html')