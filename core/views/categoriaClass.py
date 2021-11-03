import json

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core.models import Categoria


@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data["id"] = qs.id
            data["tipo"] = qs.tipo
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "tipo": nova_categoria.tipo}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.tipo = json_data["tipo"]
        qs.save()
        data = {}
        data["id"] = qs.id
        data["tipo"] = qs.tipo
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        data = {"mensagem": "Item excluido"}
        return JsonResponse(data)
