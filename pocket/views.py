import json
from .models import Pocket
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
@csrf_exempt
def add_pocket(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        pocket_name = data['pocket_name']
        pocket_budget = data['pocket_budget']
        new_pocket = Pocket(pocket_name=pocket_name, pocket_budget=pocket_budget)
        new_pocket.save()
    return JsonResponse({'isSuccessful':True},safe = False)