from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
def home_post(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)
    
def blog_post(request):
    return HttpResponse("Hello, blog!")