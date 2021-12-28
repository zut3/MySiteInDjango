from django.urls import path
from . import views


urlpatterns = [
    path('' , views.show),
    path('create' , views.show_secret)
]
