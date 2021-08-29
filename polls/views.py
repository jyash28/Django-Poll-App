from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello, world you are at the poll index.")
