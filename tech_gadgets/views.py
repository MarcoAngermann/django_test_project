from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View

from .dummy_data import gadgets

# Create your views here.

from django.views.generic.base import RedirectView

def start_page_view(request):
    return render(request, 'tech_gadgets/test.html')

from django.http import Http404

class RedirectToGadgetView(RedirectView):
    pattern_name = "single_gadget_slug_url"
    
    def get_redirect_url(self, *args, **kwargs):
        # Überprüfen, ob 'gadget_id' in kwargs vorhanden ist
        gadget_id = kwargs.get("gadget_id")
        
        # Wenn gadget_id nicht vorhanden ist, setze auf 0
        if gadget_id is None:
            gadget_id = 0
        else:
            # Überprüfen, ob gadget_id als Integer ist
            try:
                gadget_id = int(gadget_id)
            except ValueError:
                raise Http404("Gadget ID ist ungültig.")
        
        # Sicherstellen, dass gadget_id ein gültiger Index ist
        if 0 <= gadget_id < len(gadgets):
            slug = slugify(gadgets[gadget_id]["name"])
            new_kwargs = {"gadget_slug": slug}
            return super().get_redirect_url(*args, **new_kwargs)
        
        # Falls gadget_id ungültig ist, 404-Fehler zurückgeben
        raise Http404("Gadget nicht gefunden.")






def single_gadget_int_view(request, gadget_id):
    if 0 <= gadget_id < len(gadgets):
        gadget = gadgets[gadget_id]
        new_slug = slugify(gadget['name'])
        print(f"Slug für {gadget['name']}: {new_slug}")

        new_url = reverse('single_gadget_slug_url', args=[new_slug])
        print(f"Umleitung zu: {new_url}")
        return redirect(new_url)
    return HttpResponseNotFound("not found")

class GadgetView(View):
    def get(self, request, gadget_slug=""):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget['name']) == gadget_slug:
                gadget_match = gadget
                
        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"POST Data: {data}")
            return JsonResponse({'status': 'success'})
        except:
                return JsonResponse({'status': 'error'})

def single_gadget_view(request, gadget_slug=""):
    if request.method == 'GET':
         for gadget in gadgets:
            if slugify(gadget['name']) == gadget_slug:
                gadget_match = gadget
                
    if gadget_match:
            return JsonResponse(gadget_match)
            raise Http404()
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(f"POST Data: {data}")
            return JsonResponse({'status': 'success'})
        except:
                return JsonResponse({'status': 'error'})






 