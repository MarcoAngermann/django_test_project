from django.urls import path
from .views import start_page_view

urlpatterns = [
    path('', start_page_view),
]
