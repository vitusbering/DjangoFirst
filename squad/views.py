from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = ["About site", "Add information", "Feedback", "Enter"]

# Create your views here.
def index(request): # links on class HttpRequest
    #return HttpResponse("Page of application squad")
    return render(request, 'squad/index.html', {'menu': menu, 'title': 'Main page'})

def about(request):
    return render(request, 'squad/about.html', {'menu': menu, 'title': 'About site'})

def contact(request, contid):
    if(request.GET):
        print(request.GET)

    return HttpResponse(f"<h1>Contact information</h1><p>{contid}</p>")

def archive(request, year):
    if int(year) > 2022:
        #return redirect('/')# temporary redirect
        return redirect('main', permanent = True)# permanent redirect
    return HttpResponse(f"<h1> Archive by years</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')



