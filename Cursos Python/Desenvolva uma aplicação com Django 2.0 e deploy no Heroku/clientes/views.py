from django.shortcuts import render

def person_list(request):
    return render(request, 'index.html')
