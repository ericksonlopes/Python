from django.urls import path
from .views import person_list
from .views import person_new

urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    ]
