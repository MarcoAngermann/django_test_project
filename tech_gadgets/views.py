from django.shortcuts import render
from django.http import HttpResponse
import json

from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse('Hello, World!')

def single_gadget_view(request):
    return HttpResponse(json.dumps(gadgets[0]), content_type='application/json')