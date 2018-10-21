from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from .models import Pet


def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})


def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404(f"Pet Not Found {id}")
    return render(request, 'pet_detail.html', {'pet': pet})


def all_pets(request):
    pet = Pet.objects.all().values()
    return JsonResponse(list(pet), safe=False)
