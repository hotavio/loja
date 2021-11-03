from django.http import HttpResponse
from django.http.response import JsonResponse


def teste(request):
    return HttpResponse("Olá mundo do Django.")


def teste2(request):
    return HttpResponse("Uma nova página.")
