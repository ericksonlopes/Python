from django.urls import path
from .views import person_list


urlpatterns = [
    path('list/', person_list),
    ]
