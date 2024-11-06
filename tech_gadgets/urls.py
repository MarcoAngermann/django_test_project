from django.urls import path
from .views import manufacturers_view, single_gadget_int_view, GadgetView, RedirectToGadgetView ,start_page_view

urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('gadget/', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>/', RedirectToGadgetView.as_view()),
    path('gadget/<int:gadget_id>/', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>/', GadgetView.as_view(), name="single_gadget_slug_url"),
    path('manufacture/', manufacturers_view, name="all_manufacturers"), 
    path('manufacture/<int:manufacturer_id>/', manufacturers_view, name="single_manufacturer"),  
]


