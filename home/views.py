from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    

def about(request):
    return HttpResponse("about")
    

def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')
    


def donate(request):
    return render(request, 'donate.html')
    




