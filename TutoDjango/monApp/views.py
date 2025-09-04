from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bonjour !</h1>")
def home_param(request, param):
    return HttpResponse("<h1>Bonjour " + param + " !</h1>")
def contact_us(request):
    return HttpResponse(
        "<h1>Contact Us!</h1>" \
        "<form> Test </form>")

def about_us(request):
    return HttpResponse(
        "<h1>About Us!</h1>" \
        "<p>Test</p>"
    )
