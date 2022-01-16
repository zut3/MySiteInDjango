from django.urls import path
from . import views


urlpatterns = [
    path('' , views.show_main),
    path('create' , views.show_create)
]
