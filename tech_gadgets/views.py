from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def start_page_view(request):
    return HttpResponse('Hello, World!')