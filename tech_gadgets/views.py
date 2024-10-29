from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse , HttpResponseNotFound , Http404
import json
from django.utils.text import slugify
from django.urls import reverse

from .dummy_data import gadgets

# Create your views here.

def start_page_view(request):
    return HttpResponse('Hello, World!')

def single_gadget_view(request, gadget_id):
    if 0 <= gadget_id < len(gadgets):  
        gadget = gadgets[gadget_id]
        new_slug = slugify(gadget['name'])
        print(f"Slug für {gadget['name']}: {new_slug}")

        new_url = reverse('single_gadget_slug_url', args=[new_slug])
        print(f"Umleitung zu: {new_url}")
        return redirect(new_url)
    return HttpResponseNotFound("not found")

def single_gadget_slug_view(request, gadget_slug):
    gadget_match = None

    for gadget in gadgets:
        if slugify(gadget['name']) == gadget_slug:
            gadget_match = gadget
    if gadget_match:
        return JsonResponse(gadget_match)
    raise Http404("website not found")

#def single_gadget_post_view(request):
#    if request.method == 'POST':
#        try:
#            data = json.loads(request.body)
#            print(f"POST Data: {data}")
#            return JsonResponse({'status': 'success'})
#        except:
#            return JsonResponse({'status': 'error'})

def single_gadget_post_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("POST data received:", data)
            # Senden Sie eine Bestätigung zurück
            return JsonResponse({'status': 'success', 'message': 'Daten empfangen'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'JSON-Dekodierungsfehler'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Nur POST-Anfragen erlaubt'}, status=405)
 