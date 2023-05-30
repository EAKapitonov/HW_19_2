from django.urls import path

from catalog.views import index, contacts, contact

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('contact/', contact)
]
