from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {"persons": persons})

def person_new(request):
    form = PersonForm(request.POST, request.FILES, None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})